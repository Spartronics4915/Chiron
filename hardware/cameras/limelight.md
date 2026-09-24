--- 
title: Limelight Cameras
---

**Limelights** are series of pre-packaged all-in-one vision systems that are used on many FRC robots for their simplicity coupled with raw performance. They were originally made by a mentor from [FRC Team 987 (HIGHROLLER Robotics)](https://www.thebluealliance.com/team/987), and have spread to most FRC teams seeking vision solutions.

The list of **Limelights** one might encounter in today's FRC would be the `Limelight 2`, `Limelight 2+`, `Limelight 3`, `Limelight 3G`, and `Limelight 4`. **Limelight** has made it quite easy to work with these cameras from flashing to playing with capture settings, the process is simple. 

# Getting Started

To get started working with **Limelight** Cameras or any **Limelight** product in general, you first have to download the: [Limelight Hardware Manager](https://docs.limelightvision.io/docs/resources/downloads).

(flashing-os)=
# Flashing OS

Flashing to OS of your Limelight has been made extremely simple.

1. Download the latest [Limelight OS](https://docs.limelightvision.io/docs/resources/downloads) image
2. Open your `Limelight Hardware Manager` installation
3. Power off the camera
4. Hold the config button down while connecting a USB-C cable from your  laptop to the camera.

:::{note}
If the Hardware Manager cant discover the camera later on, try holding the button down for 10 seconds before plugin in the cable
:::

5. Navigate to the tab labeled: `Flash OS`
6. Select the OS image you previously installed and wait for the extraction to complete
7. Click `Select Device` then `Refresh Devices List`
8. Select your target **Limelight** from the list
9. Click `Flash Device` and wait for it to complete
10. Once complete remove the USB cable

:::{caution}
If your **Limelight** starts glitching or other strange issues arise, it is recommended to try to re-flash the camera before trying anything else. 9/10 times a simple flash will fix the issue your experiencing, if it doesn't go away consult other experienced team members or mentors. Worst case scenario contact [Limelight Support](https://limelightvision.io/pages/contact-us).
:::

# Network Configuration

## Setting the Team Number

1. Power up your robot and connect your laptop to your robot's network
2. Open the Limelight Hardware Manager, scan for Limelights, and double click the entry that appears
3. Alternatively, navigate to http://limelight.local:5801

:::{note}
If you are configuring a `Limelight 3G` or `Limelight 4` you can alternatively connect to them through USB
:::

4. Go to the "Settings" tab
5. Enter your team number and press "Update Team Number"

## Setting a Unique Hostname

:::{note}
Specifically for **Spartronics 4915**, each season we choose a naming theme for our cameras. It is quite important to stick to that specific season's theme to insure **100%** clarity
:::

1. In the settings tab navigate down to the `Hostname` box
2. Enter a unique name for each camera
3. Click `Change Hostname`

## Setting Static IP

1. Change `IP Assignment` to `Static`
2. Set IP address to `10.TE.AM.11`

    - Team **254** uses **10.2.54.xx**
    - Team **9106** uses **10.91.6.xx**
    - Team **2056** uses **10.20.56.xx**
    - Team **4915** uses **10.49.15.xx**

3. Set Netmask to `255.255.255.0`
4. Set Gateway to `10.TE.AM.1`
5. Click `Update`
6. Power-cycle your robot
7. Access your config panel at `10.TE.AM.11:5801` and camera stream at `10.TE.AM.11:5800`
8. If you are using multiple Limelights, give each Limelight a unique static IP address. Gateways and Netmasks should be the same across Limelights.

# Web Interface

(accessing_interface)=
## Accessing the Interface

After setting up your **Limelight**'s network config:

1. Power up your robot and connect your laptop to your robot's network. Alternatively you can connect to the camera through USB if using a `Limelight 3G` or `Limelight 4`.
2. Use one of these methods to access the web interface:

    - **Method 1**: Open the Limelight Hardware Manager application, scan for Limelights, and double-click on your Limelight when it appears
    - **Method 2**: Open a web browser and navigate to http://limelight.local:5801
    - **Method 3**: Open a web browser and navigate to your Limelight's static IP address with port 5801 (if configured)
    - **Method 4 (USB)**: Connect via USB-C and navigate to:
        - Windows: http://172.28.0.1:5801
        - Linux/Mac: http://172.29.0.1:5801\

## Accessible Features

Once connected, you'll have access to:

- **Settings tab**: Configure team number, hostname, and other system settings
- **Vision Pipeline tabs**: Set up and tune your vision processing pipelines
- **Camera & Crosshair tab**: Adjust camera settings and crosshair parameters
- **3D Visualization tab**: View real-time AprilTag detection and localization

All configuration is done through this web interface. Changes are saved automatically to your **Limelight**.


# Other Configurations

## Focusing the Lens

1. Power-on your robot.
2. Connect to the web interface as described in {ref}`accessing_interface`
3. Click the `Ignore NT pipeline index` to enable pipeline switching, and switch to pipeline **9**
4. Set the pipeline type to `focus`
5. Go to the configuration tab, and increase stream quality to maximum
6.Make sure the camera is pointed at something with lots of features and contrast, such as an **ARUCO board**, a detailed scene, or a **Siemen's Star**
7. Turn the lens to maximize the on-screen focus score
8. Once focused, apply **3-8 dots** of `super glue` or `super gel` around the lens

## Pipeline Setup

There are many different settings to tune to achieve optimal performance. As it would take a while to explain here is the documentation as explained by **Limelight**.

:::{note}
This section will be added later, as there is a lot to consider and write down when referencing the pipeline setup. If you have questions in the meantime reach out to SPUD42AG or Pointygreenskies.
:::

# Hardware Setup

## Mounting Limelight

:::{figure} ../../images/limelight_mounting.png
:label: limelight-mounting
:width: 80%
:align: center
:::

### Thru-Hole Mounting

- Use `1 1/4" #10-32` or `#10-24` screws with nylock nuts
- Alternatively, use `38mm M4 bolts` with nylock nuts
- Use plastic washers to preserve anodization

### Threaded Mounting (Backside)**

- 2x M3 threaded mounting points
- Consider light application of **Threadlocker**


## Wiring your Limelight

:::{figure} ../../images/limelight_wiring.webp
:label: limelight-wiring
:width: 80%
:align: center
:::

### Power

Run two 18-20AWG wires from your Limelight to a slot on your PDP, PDH, or Mini PDP. It is recommended to use a 5A or 10A breaker.

### Ethernet

Run an ethernet cable from your Limelight to your robot radio. Use twisted Cat6 cables with stranded wires (ideally 20AWG). If possible add a strain relief to your ethernet cable.

# Troubleshooting

## Status Bar Indicator

- **Slow Cylon (Scanning)**: No targets detected by the current pipeline
- **Fast Cylon (Scanning)**: Targets detected by the current pipeline
- **Slow Alternating LED Blink**: Hardware error (camera cable disconnected, sensor damage, etc.)

## Reset IP address

- Hold the config button for 10 seconds after your Limelight has booted
- Networking configuration will reset to dynamic addressing on next boot

## Flashing Limelight OS

Reference the section above all about {ref}`flashing-os`.