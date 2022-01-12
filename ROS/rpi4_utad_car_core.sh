# Inicia o modulo 'utad_car_core.launch' com servidor de ROS no Raspberry PI 4

export ROS_MASTER_URI=http://rpi4:11311

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws

roslaunch utad_car_core utad_car_core.launch
