---
title: Using Target Data
---

Java and C++ include a `PhotonUtils` class containing common calculations that turn raw camera and target measurements into more useful field information. PhotonLibPy does not currently include this class, but the same calculations can be performed with `math` and WPIMath.

# Estimating Field-Relative Pose with AprilTags

`estimateFieldToRobotAprilTag(cameraToTarget, fieldRelativeTagPose, cameraToRobot)` calculates the robot's `Pose3d` on the field. It combines:

- The transform from the camera to the detected AprilTag
- The known field-relative pose of that AprilTag
- The transform from the camera to the robot's origin

In Python, get the tag's known field pose and apply the inverse camera-to-target and robot-to-camera transforms:

:::python
fieldRelativeTagPose = fieldLayout.getTagPose(target.getFiducialId())

if fieldRelativeTagPose is not None:
    cameraToTarget = target.getBestCameraToTarget()
    cameraToRobot = robotToCamera.inverse()

    robotPose = (
        fieldRelativeTagPose
        .transformBy(cameraToTarget.inverse())
        .transformBy(cameraToRobot)
    )
:::

For most AprilTag localization, the [`PhotonPoseEstimator`](pose_estimation.md) described on the next page is the easier and more complete solution because it can combine multiple tags and handle result timestamps for you.

# Estimating Field-Relative Pose Traditionally

`estimateFieldToRobot()` estimates the robot's `Pose2d` using the camera and target heights, camera and target pitch, target yaw, the robot's gyro angle, the known target pose, and the camera's position on the robot.

Internally, this first estimates the target's position relative to the camera from its pitch and yaw. It then uses the gyro to rotate that measurement into the field coordinate system.

:::python
import math
import wpimath

cameraHeightMeters = 0.5
targetHeightMeters = 1.45
cameraPitchRadians = math.radians(20.0)
targetPitchRadians = math.radians(target.getPitch())

# PhotonVision yaw is clockwise-positive, so negate it for WPIMath
targetYawRadians = math.radians(-target.getYaw())

distanceMeters = (targetHeightMeters - cameraHeightMeters) / math.tan(
    cameraPitchRadians + targetPitchRadians
)

cameraToTargetTranslation = wpimath.Translation2d(
    math.cos(targetYawRadians) * distanceMeters,
    math.sin(targetYawRadians) * distanceMeters,
)

# Replace this with the known Pose2d of the target on the field
fieldRelativeTargetPose = wpimath.Pose2d(
    8.0,
    4.0,
    wpimath.Rotation2d(),
)

gyroAngle = self.gyro.getRotation2d()
cameraToTarget = wpimath.Transform2d(
    cameraToTargetTranslation,
    wpimath.Rotation2d(
        -gyroAngle.radians() - fieldRelativeTargetPose.rotation().radians()
    ),
)

# Camera is mounted 0.5m in front of the robot's origin
robotToCamera2d = wpimath.Transform2d(
    wpimath.Translation2d(0.5, 0.0),
    wpimath.Rotation2d(),
)

robotPose = (
    fieldRelativeTargetPose
    .transformBy(cameraToTarget.inverse())
    .transformBy(robotToCamera2d.inverse())
)
:::

# Calculating Distance to a Target

If both the camera height and target height are fixed, the distance between them can be calculated from the camera mounting pitch and the measured pitch to the target. This calculation assumes that the camera and target are at known, different heights.

:::python
import math

cameraHeightMeters = 0.5
targetHeightMeters = 1.45
cameraPitchRadians = math.radians(20.0)
targetPitchRadians = math.radians(target.getPitch())

distanceMeters = (targetHeightMeters - cameraHeightMeters) / math.tan(
    cameraPitchRadians + targetPitchRadians
)
:::

:::{warning}
This method requires the camera to have no roll and the camera and target to be at different heights. A larger height difference will generally produce a more stable distance estimate.
:::

# Calculating Distance Between Two Poses

`getDistanceToPose(robotPose, targetPose)` calculates the straight-line distance between two `Pose2d` objects. This is useful when the AprilTag is not mounted directly on the location that the robot needs to approach.

:::python
distanceToTarget = robotPose.translation().distance(
    targetPose.translation()
)
:::

# Estimating Camera Translation to a Target

`estimateCameraToTargetTranslation(distance, targetYaw)` returns a `Translation2d` from the camera to the target using the previously calculated distance and the target's yaw.

:::python
import math
import wpimath

targetYawRadians = math.radians(-target.getYaw())

cameraToTargetTranslation = wpimath.Translation2d(
    math.cos(targetYawRadians) * distanceMeters,
    math.sin(targetYawRadians) * distanceMeters,
)
:::

:::{note}
PhotonVision yaw follows computer-vision conventions, so the yaw must be negated when converting it to WPILib's standard mathematical convention. In WPILib, counter-clockwise angles are positive.
:::

# Getting the Yaw to a Pose

`getYawToPose(robotPose, targetPose)` returns the `Rotation2d` between the robot and an arbitrary field-relative target. This can be used to aim at a location even when an AprilTag is not placed directly on it.

:::python
import wpimath

relativeTranslation = targetPose.relativeTo(robotPose).translation()
yawToTarget = wpimath.Rotation2d(
    relativeTranslation.X(),
    relativeTranslation.Y(),
)
:::

