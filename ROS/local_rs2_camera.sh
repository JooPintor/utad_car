
#export ROS_MASTER_URI=http://rpi4:11311
export ROS_MASTER_URI=http://localhost:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws
#roslaunch realsense2_camera rs_camera.launch
roslaunch realsense2_camera rs_d435_camera_with_model.launch
