
#export ROS_MASTER_URI=http://rpi4:11311
export ROS_MASTER_URI=http://localhost:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws
roslaunch utad_car_bringup utad_car.launch
