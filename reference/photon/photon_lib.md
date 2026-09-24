---
title: Photon Library
---

**Photon Vision** is a open source vision library for `FRC robotics`, meant to be simple to implement while being compatible with a wide variety of coprocessors and cameras. While not as popular as simpler plug-in-play solutions like **Limelights**, it's flexibility and customization has made it a stand out solution in modern `FRC`. 

Generally if you see a camera and processor other than a Limelight on a team's robot, its safe to assume its running **Photon Vision**; it's rare to see custom solutions other than these two. It is built on top of **OpenCV**, which means much of its algorithms and processes stay up to date, especially as it is coupled with an extremely active dev team.

# Getting Started

To set up photon vision in your RobotPy project it is as simple as including the dependency in your `pyproject.toml`:

:::python
# Other pip packages to install
requires = [
    "photonlibpy",
]
:::

# Programming Reference

- [Getting Target Data](getting_target_data.md)
- [Using Target Data](using_target_data.md)
- [AprilTags and PhotonPoseEstimator](pose_estimation.md)
- [Camera Controls](camera_controls.md)
- [Simulation](simulation.md)

