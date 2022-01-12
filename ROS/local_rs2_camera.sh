# Inicia o modulo 'rs_d435_camera_with_model.launch' com servidor de ROS local

export ROS_MASTER_URI=http://localhost:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws

roslaunch realsense2_camera rs_d435_camera_with_model.launch
