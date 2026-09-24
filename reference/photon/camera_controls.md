---
title: Camera Controls
---

# Driver Mode and Pipeline Index/Latency

Once a `PhotonCamera` has been created, robot code can switch between vision pipelines, enable driver mode, and read the processing latency.

## Toggling Driver Mode

Driver mode provides an unfiltered camera view intended for the driver instead of processing the image through a vision pipeline.

:::python
# Enable driver mode
self.camera.setDriverMode(True)
:::

## Setting the Pipeline Index

Use `setPipelineIndex()` to switch pipelines while the robot is running. The index must match the pipeline number shown in the PhotonVision UI.

:::python
# Switch to pipeline 2
self.camera.setPipelineIndex(2)
:::

## Getting Pipeline Latency

Pipeline latency is stored on the `PhotonPipelineResult` and represents the time PhotonVision spent processing the frame.

:::python
latencyMilliseconds = result.getLatencyMillis()
latencySeconds = latencyMilliseconds / 1000.0
captureTimestamp = result.getTimestampSeconds()
:::

The capture timestamp is more useful than the current time when adding a vision measurement to a pose estimator because it allows WPILib to compensate for camera and processing delay.

## Camera Status and Control

`PhotonCamera` can report its current state and whether PhotonVision is actively sending frames. A camera is enabled by default, but it can be temporarily disabled to stop its processing.

:::python
cameraName = self.camera.getName()
isConnected = self.camera.isConnected()
isEnabled = self.camera.getEnabled()
isDriverMode = self.camera.getDriverMode()
activePipeline = self.camera.getPipelineIndex()

# Temporarily disable or re-enable camera processing
self.camera.setEnabled(False)
self.camera.setEnabled(True)
:::

:::{warning}
`isConnected()` verifies that the camera is actively returning new data, not just that a NetworkTables topic with its name exists. Use it when reporting camera health to the driver station.
:::

# Controlling LEDs

Supported PhotonVision hardware allows its vision LEDs to be controlled through `PhotonCamera.setLEDMode()`. The available `VisionLEDMode` values are `kOff`, `kOn`, `kBlink`, and `kDefault`. The default mode follows the LED setting of the selected pipeline.

:::python
from photonlibpy.photonCamera import VisionLEDMode

# Blink the camera's vision LEDs
self.camera.setLEDMode(VisionLEDMode.kBlink)

# Read the current LED mode
ledMode = self.camera.getLEDMode()
:::

# FPS Limiter

The FPS limiter reduces how many frames a camera processes each second. It is intended to save power, especially when using a high-frame-rate camera with a powerful coprocessor.

:::python
# Read the current limit
limit = self.camera.getFPSLimit()

# Process at most 10 frames per second
self.camera.setFPSLimit(10)

# Remove the limit
self.camera.setFPSLimit(-1)
:::

The default value is `-1`, which disables the limiter and allows PhotonVision to process frames as quickly as it normally would.

