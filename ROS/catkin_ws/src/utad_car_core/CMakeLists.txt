cmake_minimum_required(VERSION 3.1)
project(utad_car_core)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  compressed_image_transport
  roscpp
  std_msgs
  geometry_msgs
  rospy
  tf
  tf2_ros
  dynamic_reconfigure
)
find_package(Boost REQUIRED)
#catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

#add_message_files(
#  DIRECTORY msg
#  FILES
#)

#generate_messages(
#  DEPENDENCIES
#  std_msgs
#  geometry_msgs
#)

#add dynamic reconfigure api
generate_dynamic_reconfigure_options(

)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  INCLUDE_DIRS
  LIBRARIES
  CATKIN_DEPENDS
    message_runtime
    rospy
    tf
    tf2_ros
    std_msgs
    geometry_msgs
  DEPENDS Boost
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination

#install(PROGRAMS
catkin_install_python(PROGRAMS
  nodes/motion
  nodes/odometer
  nodes/car_tf2_broadcast
  
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY
  launch
  nodes
  scripts
  msg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
if(CATKIN_ENABLE_TESTING)

endif()

