# ENPM661 Competition
# **Competition Video** 👇

[![Competition Video*](https://img.youtube.com/vi/m-B26ImnQ5g/0.jpg)](https://youtu.be/m-B26ImnQ5g)

## Overview

This repository contains a ROS2-based navigation system that enables a robot to traverse a predefined set of waypoints through a maze. Currently, the waypoints are hardcoded, but the system is designed to be extended with a path planning algorithm.

## Features

- **Odometry-Based Navigation:** Uses odometry data from the `/odom` topic to determine the robot’s position and orientation.
- **Velocity Control:** Publishes velocity commands to the `/cmd_vel` topic to move towards the target waypoints.
- **Turn and Move Logic:** Computes angular and linear velocity adjustments to reach each waypoint.
- **Future Path Planning Integration:** The waypoint list will be dynamically generated using a path planning algorithm.

## Code Structure

- `OdomSubscriber`: Subscribes to odometry data and extracts position and orientation.
- `move(goal)`: Moves the robot towards a specified goal point.
- `turn(g_ang, g_direc)`: Rotates the robot to a desired angle.
- `angle_finder(goal_coord)`: Computes the required turning angle to face a goal.
- `good_theta(cur_ang, to_ang)`: Determines the optimal turning direction.
- `go_2_points()`: Executes navigation through the predefined waypoints.
- `main()`: Initializes the ROS2 node and starts navigation.


## Running the Code

1. Ensure ROS2 is installed and sourced.
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
3. Build and run the ROS2 package:
   ```sh
   colcon build
   source install/setup.bash
   ros2 run your_package_name odom_sub2
   ```

## Future Work: Path Planning

The next step is to replace the hardcoded waypoints with a path planning algorithm, which will generate optimal routes dynamically based on maze structure.

