---
title: AprilTags and PhotonPoseEstimator
---

`PhotonPoseEstimator` combines data from the AprilTags visible to a camera to estimate the robot's field-relative pose. Each camera on the robot needs its own `PhotonPoseEstimator` instance.

# Creating an AprilTag Field Layout

An `AprilTagFieldLayout` stores the known position of every AprilTag in a space. WPILib provides layouts for official FRC fields, though you can also load a custom JSON layout for a practice field, classroom, or shop.

:::python
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout

fieldLayout = AprilTagFieldLayout.loadField(AprilTagField.kDefaultField)
:::

# Defining the Robot-to-Camera Transform

The pose estimator must know where the camera is mounted relative to the robot's origin. This is represented by a `Transform3d` containing a `Translation3d` in meters and a `Rotation3d`.

:::python
import wpimath

# Camera is 0.5m forward and 0.5m above the robot origin,
# angled 30 degrees upward.
robotToCamera = wpimath.Transform3d(
    wpimath.Translation3d(0.5, 0.0, 0.5),
    wpimath.Rotation3d.fromDegrees(0.0, -30.0, 0.0),
)
:::

:::{warning}
Measure the camera transform carefully. An inaccurate camera position or rotation will produce an inaccurate robot pose.
:::

# Creating a PhotonPoseEstimator

Create the camera and pass the field layout and robot-to-camera transform into `PhotonPoseEstimator`:

:::python
from photonlibpy import PhotonCamera, PhotonPoseEstimator

self.camera = PhotonCamera("YOUR CAMERA NAME")
self.cameraPoseEstimator = PhotonPoseEstimator(fieldLayout, robotToCamera)
:::

# Pose Estimation Strategies

The complete Java and C++ versions of `PhotonPoseEstimator` provide several strategies through methods following the `estimate<strategy>Pose()` naming pattern:

- `estimateCoprocMultiTagPose()` combines all visible tag corners on the coprocessor. This is the recommended and most accurate strategy.
- `estimateLowestAmbiguityPose()` selects the target pose with the lowest ambiguity.
- `estimateClosestToCameraHeightPose()` selects the pose closest to the camera's known height.
- `estimateClosestToReferencePose()` selects the pose closest to a supplied reference pose.
- `estimateAverageBestTargetsPose()` averages the best pose from each visible target.
- `estimateRioMultiTagPose()` performs multi-tag estimation on the roboRIO. It is older, slower, and not recommended.
- `estimatePnpDistanceTrigSolvePose()` uses the best target's distance and the robot heading. It requires fresh heading data every frame through `addHeadingData()`.
- `estimateConstrainedSolvepnpPose()` assumes the drivetrain is flat on the floor and solves a constrained Perspective-n-Point problem on the roboRIO. It also requires fresh heading data every frame.

:::{note}
In PhotonLibPy `v2027.0.0-alpha-2`, the implemented strategies are `estimateCoprocMultiTagPose()`, `estimateLowestAmbiguityPose()`, and `estimatePnpDistanceTrigSolvePose()`. The other strategies above are not yet available in Python.
:::

When using `estimatePnpDistanceTrigSolvePose()`, add timestamped robot-heading samples every loop. Clear and reseed this buffer whenever the robot pose or gyro heading is reset:

:::python
timestamp = wpilib.Timer.getFPGATimestamp()
heading = self.gyro.getRotation2d()

self.cameraPoseEstimator.addHeadingData(timestamp, heading)

for result in self.camera.getAllUnreadResults():
    estimatedPose = (
        self.cameraPoseEstimator.estimatePnpDistanceTrigSolvePose(result)
    )
:::

After resetting the robot pose or gyro, clear the old heading samples and add the new heading as the first sample:

:::python
timestamp = wpilib.Timer.getFPGATimestamp()
heading = self.gyro.getRotation2d()
self.cameraPoseEstimator.resetHeadingData(timestamp, heading)
:::

Start with coprocessor multi-tag estimation and fall back to a single-tag strategy when a multi-tag estimate is unavailable:

:::python
for result in self.camera.getAllUnreadResults():
    estimatedPose = self.cameraPoseEstimator.estimateCoprocMultiTagPose(result)

    if estimatedPose is None:
        estimatedPose = self.cameraPoseEstimator.estimateLowestAmbiguityPose(result)
:::

An estimate may be `None` when there are no visible tags, too few tags for the selected strategy, required heading data is missing, or a solver fails. A valid `EstimatedRobotPose` contains both the calculated `Pose3d` and the timestamp at which the image was captured.

# Adding the Vision Measurement

Feed every valid estimate into the drivetrain's pose estimator using its timestamp. This allows WPILib to combine the vision measurement with wheel odometry and gyro data.

:::python
for result in self.camera.getAllUnreadResults():
    estimatedPose = self.cameraPoseEstimator.estimateCoprocMultiTagPose(result)

    if estimatedPose is None:
        estimatedPose = self.cameraPoseEstimator.estimateLowestAmbiguityPose(result)

    if estimatedPose:
        self.swerve.addVisionPoseEstimate(
            estimatedPose.estimatedPose,
            estimatedPose.timestampSeconds,
        )
:::

