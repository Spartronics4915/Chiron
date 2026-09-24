"""Deterministic lifecycle checks for the course's final intake example."""
import commands2
import hal
import pytest
from wpilib.simulation import DriverStationSim, pauseTiming, resumeTiming, stepTiming
from examples.support.intake_io import IntakeSim
from examples.mechanism.solution.intake_subsystem import Intake
from examples.mechanism.solution.intake_commands import Acquire, Release, ManualIntake


@pytest.fixture
def rig():
    hal.initialize(500, 0)
    commands2.CommandScheduler.resetInstance()
    pauseTiming()
    DriverStationSim.resetData()
    DriverStationSim.setDsAttached(True)
    DriverStationSim.setEnabled(True)
    DriverStationSim.notifyNewData()
    scheduler = commands2.CommandScheduler.getInstance()
    io = IntakeSim()
    io.enabled = True
    intake = Intake(io)

    def tick(count):
        for _ in range(count):
            stepTiming(0.02)
            DriverStationSim.notifyNewData()
            scheduler.run()
            io.step()

    yield io, intake, tick
    scheduler.cancelAll()
    scheduler.unregisterAllSubsystems()
    commands2.CommandScheduler.resetInstance()
    DriverStationSim.setEnabled(False)
    DriverStationSim.notifyNewData()
    resumeTiming()


def test_acquire_success_and_stop(rig):
    io, intake, tick = rig
    command = Acquire(intake)
    command.schedule()
    tick(30)
    assert command.succeeded
    assert not command.isScheduled()
    assert io.detected and io.output == 0


def test_timeout_is_not_success(rig):
    io, intake, tick = rig
    io.piece_available = False
    command = Acquire(intake, timeout=0.2)
    command.schedule()
    tick(20)
    assert not command.succeeded and not command.isScheduled()
    assert not io.detected and io.output == 0


def test_conflicting_requirement_interrupts_acquire(rig):
    io, intake, tick = rig
    acquire = Acquire(intake)
    acquire.schedule()
    tick(2)
    release = Release(intake)
    release.schedule()
    assert not acquire.isScheduled()
    assert not acquire.succeeded and io.output == 0
    tick(2)
    assert not release.isScheduled()
    assert io.output == 0


def test_release_held_piece(rig):
    io, intake, tick = rig
    io.detected = True
    command = Release(intake)
    command.schedule()
    tick(30)
    assert not io.detected and io.output == 0
    assert not command.isScheduled()


def test_disabled_and_cancel_cleanup(rig):
    io, intake, tick = rig
    command = Acquire(intake)
    command.schedule()
    tick(2)
    command.cancel()
    assert io.output == 0
    command.schedule()
    tick(2)
    io.enabled = False
    DriverStationSim.setEnabled(False)
    tick(2)
    assert not command.isScheduled()
    assert io.output == 0 and not command.succeeded


def test_reschedule_resets_timer_and_success(rig):
    io, intake, tick = rig
    command = Acquire(intake, timeout=0.1)
    io.detected = True
    command.schedule()
    tick(2)
    assert command.succeeded
    io.detected = False
    io.piece_available = False
    tick(50)
    command.schedule()
    assert not command.succeeded
    tick(2)
    assert command.isScheduled()
    tick(10)
    assert not command.isScheduled() and not command.succeeded


def test_default_reads_live_value_and_resumes(rig):
    io, intake, tick = rig
    request = [0.2]

    def read_request():
        return request[0]

    default = ManualIntake(intake, read_request)
    intake.setDefaultCommand(default)
    tick(3)
    assert io.output == 0.2
    command = Acquire(intake)
    command.schedule()
    assert not default.isScheduled()
    tick(2)
    request[0] = -0.3
    command.cancel()
    tick(3)
    assert default.isScheduled() and io.output == -0.3


def test_subsystem_limits_and_independent_instances(rig):
    io, intake, _ = rig
    intake.set_output(2)
    assert io.output == 1
    io.detected = True
    intake.set_output(2)
    assert io.output == 0
    intake.set_output(-2)
    assert io.output == -1
    other = Intake(IntakeSim())
    assert not other.has_piece()
