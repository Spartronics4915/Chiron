---
title: Simulation
---

# Simulation Support in Python

Although the `v2027.0.0-alpha-2` documentation page says Python simulation is not supported yet, the matching PhotonLibPy source includes a working simulation API. The primary classes are:

- `VisionSystemSim`, which manages simulated cameras, targets, and robot poses
- `PhotonCameraSim`, which publishes simulated results to a normal `PhotonCamera`
- `SimCameraProperties`, which configures resolution, field of view, frame rate, latency, and calibration error
- `VisionTargetSim`, which represents a custom field target

# Setting Up a Simulated Camera

Create the normal `PhotonCamera` first so real and simulated code read results through the same interface. Then create the simulated vision system and attach the camera at the same robot-to-camera transform used by `PhotonPoseEstimator`.

:::python
from photonlibpy.simulation import (
    PhotonCameraSim,
    SimCameraProperties,
    VisionSystemSim,
)

self.visionSim = VisionSystemSim("main")

# Choose the preset closest to the real camera and resolution
cameraProperties = SimCameraProperties.OV9281_1280_720()
self.cameraSim = PhotonCameraSim(
    self.camera,
    cameraProperties,
    fieldLayout,
)

self.visionSim.addCamera(self.cameraSim, robotToCamera)
self.visionSim.addAprilTags(fieldLayout)
:::

`SimCameraProperties` can also be created manually when none of the presets match the real camera:

:::python
import wpimath

cameraProperties = SimCameraProperties()
cameraProperties.setCalibrationFromFOV(
    1280,
    720,
    wpimath.Rotation2d.fromDegrees(90.0),
)

# Average and standard deviation of calibration error in pixels
cameraProperties.setCalibError(0.25, 0.05)

cameraProperties.setFPS(30.0)
cameraProperties.setExposureTime(10.0e-3)
cameraProperties.setAvgLatency(60.0e-3)
cameraProperties.setLatencyStdDev(20.0e-3)
:::

# Updating the Simulation

Call `VisionSystemSim.update()` periodically with the drivetrain simulation's ground-truth `Pose2d` or `Pose3d`. Do not pass the vision-corrected estimated pose back into the simulation.

:::python
def simulationPeriodic(self) -> None:
    # Replace this with the drivetrain simulation's ground-truth pose getter
    simulatedRobotPose = self.swerve.getSimulationPose()
    self.visionSim.update(simulatedRobotPose)
:::

The simulated results are published through NetworkTables, so the existing calls to `getAllUnreadResults()` and `PhotonPoseEstimator` work without a separate simulation-only data path. The simulated field is also published to SmartDashboard as `VisionSystemSim-main/Sim Field`.

For a camera mounted on a moving turret or gimbal, update its transform with `adjustCamera()`:

:::python
newRobotToCamera = wpimath.Transform3d(
    wpimath.Translation3d(0.5, 0.0, 0.5),
    wpimath.Rotation3d(0.0, turretPitchRadians, turretYawRadians),
)

self.visionSim.adjustCamera(self.cameraSim, newRobotToCamera)
:::

`addVisionTargets()` can add custom reflective, colored-shape, fiducial, or object-detection targets when the standard AprilTag layout is not enough:

:::python
from photonlibpy.estimation import TargetModel
from photonlibpy.simulation import VisionTargetSim

targetPose = wpimath.Pose3d(
    wpimath.Translation3d(8.0, 4.0, 1.0),
    wpimath.Rotation3d(),
)
targetModel = TargetModel.createPlanar(0.5, 0.5)
simulatedTarget = VisionTargetSim(targetPose, targetModel)

self.visionSim.addVisionTargets(
    [simulatedTarget],
    "customTargets",
)
:::

# Hardware-in-the-Loop Simulation

Hardware-in-the-loop simulation uses a real coprocessor running PhotonVision while the robot program runs in WPILib simulation on a computer. This is useful for developing and validating code before the camera is installed on the robot.

Before starting, install PhotonVision on the coprocessor and connect both the coprocessor and simulation computer to the same network, such as a home router.

:::{warning}
Connecting the coprocessor directly to the computer will not work for this setup. Both devices must be connected through the same network.
:::

To configure the connection:

1. Open the PhotonVision web UI.
2. Select `Settings` in the sidebar.
3. Find `Team Number/NetworkTables Server Address` under the networking settings.
4. Replace the normal team number with the IP address of the computer running simulation.
5. Start the robot simulation and confirm that the PhotonVision table appears in the NetworkTables dashboard.

On Windows, use `ipconfig` in Command Prompt to find the computer's IPv4 address:

:::console
C:\Users\you> ipconfig

Ethernet adapter Ethernet:
   IPv4 Address. . . . . . . . . . . : 192.168.254.13
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.254.254
:::

No robot-code changes are required. Once connected, PhotonLib should behave similarly to normal operation.

