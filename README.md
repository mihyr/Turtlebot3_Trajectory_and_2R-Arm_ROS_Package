# Turtlebot3 Figure-Eight and 2R Arm ROS Package
## Overview

### *Turtlebot3 Figure-Eight Trajectory*
This package makes the turtlebot to follow a figure-8 trajectory (in Gazebo as well as in real world).

* The Robot begins in a paused state and orients itself in direction of motion, relative to `odom` frame.
* To start/resume motion, type `rosservice call /resume_turtle`. To pause, type `rosservice call /pause_turtle`
* The user has an option to run the code on actual Turtlebot3: Burger or in Gazebo. User may visualize the robot in RVIZ optionally in both the cases. Figure-8 trajectory size is configurable. 

### *2R Arm in RVIZ*
This package uses RViZ to visualize a Xacro URDF of a Robot arm and making it's end-effector follow a linear trajectory.

## Dependencies
Title | Link
------------ | -------------
turtlebot3_gazebo| [ROS Wiki](http://wiki.ros.org/turtlebot3_bringup)
turtlebot3_bringup | [ROS Wiki](http://wiki.ros.org/turtlebot3_bringup)


## Installation Instructions
* Create a catkin workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
```
* Clone the repo into `catkin_ws/src`
```
git clone https://github.com/ME495-EmbeddedSystems/homework02-whomihirpatel.git
```
* Build the workspace and activate it
```
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.zsh

```

## Usage Instructions
## *Turtlebot3 Figure-Eight Trajectory*
* To run the code on actual turtlebot:
    * Launch Roscore on remote PC (your computer)
        ```
        roscore
        ```
    * In a seperate terminal, ssh into turtlebot and launch the startup file
        ```
        ssh foo@turtlebot.local
        roslaunch turtlebot3_bringup turtlebot3_robot.launch
        ```
    * On remote PC Export the turtlebot model and run the figure_eight.launch file
        ```
        export TURTLEBOT3_MODEL=burger
        roslaunch homework2 figure_eight.launch 
        ```
    * Note: By default, the figure_eight.launch will not launch GAZEBO or RVIZ or Rqt_graph, but can be launched optionally, check configuration options below.
    
    * The turtlebot is in pause state by-default, to start/resume motion, type 
        ```
        rosservice call /resume_turtle
        ```
     * To pause, type 
        ```
        rosservice call /pause_turtle
        ```
* To run the code in Gazebo:
    * Run the following launchfile
        ```
        roslaunch homework2 figure_eight.launch gazebo:=true  
        ```
    * To start motion, type
        ```
        rosservice call /resume_turtle
        ```

### Configurations Instructions for Turtlebot3

* `gazebo:=true` option to run the code on gazebo
* `rviz:=true ` option to view robot in RVIZ (This applies to both, realworld code as well as gazebo)
* `rqt_odom:=true ` option to plot odom data from real robot/gazebo in realtime
* `rqt_calculated:=true` option to plot calculated x,y position in realtime
*  user may alter `height`, `width`, `time to complete loop` as well as `frequency` parameters for figure-eight, from `config/trajectory.yaml`

    Add the above mentioned args to launch file in any combination desired, for eg. command below will launch code on actual robot and load rviz for visualizaion on remote PC as well as plot odom data on rqt_graph
    ```
    roslaunch homework2 figure_eight.launch rviz:=true rqt_odom:=true 
    ```
* Demo: Click on the image below to view video: *Turtlebot3 Following Figure-8 Trajectory: Visualization in GAZEBO*

    [![Watch the video](https://img.youtube.com/vi/h6xmesHbBHA/maxresdefault.jpg )](https://youtu.be/h6xmesHbBHA)

* Demo: Click on the image below to view video: *Turtlebot3 Following Figure-8 Trajectory: Visualization in RVIZ*

    [![Watch the video](https://img.youtube.com/vi/DA9sDGc_mRw/maxresdefault.jpg )](https://youtu.be/DA9sDGc_mRw)

* Demo: Click on the image below to view video: *Turtlebot3 Following Figure-8 Trajectory: Real World*
    [![Watch the video](https://img.youtube.com/vi/WVT1hkNHyvA/maxresdefault.jpg )](https://youtu.be/WVT1hkNHyvA)
---
## *2R Arm in RVIZ*

* Use the command below to visualize 2R Robot arm in RVIZ following a trajectory with markers
    ```
    roslaunch homework2 arm_mark.launch

    ```
* Use the command below to launch 2R simulation in RVIZ with manual control GUI (make sure to add arg `gui:=true` to load joint_state_publisher node)
    ```
    roslaunch homework2 arm_basics.launch gui:=true 
    ```

 * Demo: Click on the image below to view video: 2R arm simulation: with marker

    [![Watch the video](https://img.youtube.com/vi/mWqHMz_zE3Y/maxresdefault.jpg )](https://youtu.be/mWqHMz_zE3Y)


 * Demo: Click on the image below to view video: 2R arm simulation: manual Control
 
    [![Watch the video](https://img.youtube.com/vi/PP-TFPdcaN4/maxresdefault.jpg )](https://youtu.be/PP-TFPdcaN4)
----