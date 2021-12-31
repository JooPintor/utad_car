
export ROS_MASTER_URI=http://rpi4.local:11311
#export ROS_MASTER_URI=http://localhost:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws
roslaunch realsense2_camera rs_camera.launch enable_sync:=true
#roslaunch realsense2_camera rs_camera.launch filters:=pointcloud enable_infra:=true depth_width:=424 infra_width:=424 color_width:=424 depth_height:=240 infra_height:=240 color_height:=240 depth_fps:=30 color_fps:=30 infra_fps:=30
#roslaunch realsense2_camera rs_d435_camera_with_model.launch
#roslaunch realsense2_camera rs_d435_camera_with_model.launch filters:=pointcloud enable_infra1:=false enable_infra2:=false
#roslaunch realsense2_camera rs_camera.launch filters:=pointcloud enable_infra1:=false enable_infra2:=false
#roslaunch realsense2_camera rs_camera.launch enable_infra1:=false enable_infra2:=false
#roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
