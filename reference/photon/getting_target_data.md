---
title: Getting Target Data
---

# Constructing a Camera

The first step to getting data from the targets in your camera's feed is to actually create the camera in code:

:::python
# Change this to match the name of your camera as shown in the web ui
self.camera = PhotonCamera("your_camera_name_here")
:::

:::{note}
In PhotonLibPy, the `PhotonCamera` constructor takes the camera name that PhotonVision broadcasts over NetworkTables. This must exactly match the camera's nickname in the PhotonVision UI, and every camera must have a unique name even when they are attached to different coprocessors.
:::

Through the `PhotonCamera` class, you can retrieve yaw, pitch, roll, robot-relative pose, latency, and a wealth of other information.

# Getting a Pipeline Result

You may be asking yourself, what is a Photon Pipeline Result? Well, A `PhotonPipelineResult` is a container that contains all information about currently detected targets from a `PhotonCamera`. You can retrieve the latest pipeline result using the PhotonCamera instance.

To get a `PhotonPipelineResult` from your camera there are two methods:

:::python
# Method 1: Query the latest result from PhotonVision
result = self.camera.getLatestResult()

# Method 2: Query the list of pipeline results sent by PhotonVision since the last call of this function
results = self.camera.getAllUnreadResults()
:::

:::{warning}
If you are trying to get one or multiple result(s) from your camera it is always best to use `Method 2`, as currently the `getLatestResult()` function can **miss results**, or provide **duplicate** ones. Though it is important to only call `getAllUnreadResults()` once per-camera per-loop, but often enough to keep results fresh. 
:::

# Checking for Targets

Each pipeline result has a `hasTargets()` method to inform you as to whether the result contains any targets.

:::python
hasTargets = result.hasTargets()
:::

:::{warning}
In Python, you should _always_ check if the result has a target via `hasTargets()` before getting targets or else you may get an `AttributeError`. Further, you must use the same result in every subsequent call in that loop.
:::

# Getting Tracked Targets

A tracked target contains information about each target from a pipeline result. This information includes yaw, pitch, area, and the camera-to-target transform.

You can get a list of tracked targets using the `getTargets()` method from a pipeline result:

:::python
# Get a list of currently tracked targets.
targets = result.getTargets()
:::

To get the best target you can use the `getBestTarget()` method from a pipeline result:

:::python
target = result.getBestTarget()
:::

# Getting Target Data

To get the data from a `PhotonTrackedTarget` there are a bunch of simple getter methods you can use:

:::python
yaw = target.getYaw()
pitch = target.getPitch()
area = target.getArea()
skew = target.getSkew()
pose = target.getBestCameraToTarget()
corners = target.getDetectedCorners()
boundingBoxCorners = target.getMinAreaRectCorners()
:::

- `getYaw()` returns the target yaw in degrees, with left being positive.
- `getPitch()` returns the target pitch in degrees, with up being positive.
- `getArea()` returns the percentage of the image covered by the target's bounding box, from `0-100`.
- `getSkew()` returns the target skew in degrees, with counter-clockwise being positive.
- `getBestCameraToTarget()` returns the lowest-error `Transform3d` from the camera to the target.
- `getDetectedCorners()` returns the detected target corners.
- `getMinAreaRectCorners()` returns the four corners of the smallest rectangular bounding box around the target.

# Getting AprilTag Data

AprilTag targets provide a few additional values on top of the standard target data. `getFiducialId()` returns the ID of the detected tag, while `getPoseAmbiguity()` describes how uncertain the pose solve is. A lower ambiguity value means the result is more trustworthy.

PhotonVision also provides both the best and alternate camera-to-target transforms. The best transform has the lowest reprojection error, while the alternate transform has the highest.

:::python
targetID = target.getFiducialId()
poseAmbiguity = target.getPoseAmbiguity()
bestCameraToTarget = target.getBestCameraToTarget()
alternateCameraToTarget = target.getAlternateCameraToTarget()
:::

:::{note}
All of the standard target data above, except skew, is also available when tracking AprilTags.
:::

# Saving Pictures to File

A `PhotonCamera` can save still images from either the raw input stream or the processed output stream. This is particularly useful when debugging what the camera saw on the field or confirming that a target was identified correctly.

:::python
# Capture a pre-process camera stream image
self.camera.takeInputSnapshot()

# Capture a post-process camera stream image
self.camera.takeOutputSnapshot()
:::

Saved images are stored in PhotonVision's configuration directory. To retrieve them, use the `Export` operation in the settings tab and open the downloaded `.zip` file.

:::{note}
Saving an image takes time and disk space. PhotonVision will only save one image every `500ms`, even if these methods are called more frequently. It is best to connect snapshots to a controller button or a specific point in an autonomous routine.
:::

