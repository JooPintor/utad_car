
export ROS_MASTER_URI=http://localhost:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws
roslaunch utad_car_navigation utad_car_navigation.launch
