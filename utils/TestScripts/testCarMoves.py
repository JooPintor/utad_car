#!/usr/bin/env python

import time
import rospy
import roslib

from geometry_msgs.msg import Twist

rospy.init_node("test")

move = rospy.Publisher('cmd_vel', Twist, queue_size=4)

time.sleep(1)

# Now we're going to move the robot
print('Moving forward for 5 seconds')
move_msg = Twist()
move_msg.linear.x = 1
move.publish(move_msg)
time.sleep(5.0)

print('Moving backward for 5 seconds')
move_msg = Twist()
move_msg.linear.x = -1
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot right for 5 seconds')
move_msg = Twist()
move_msg.linear.x = 0
move_msg.angular.z = 2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot left for 5 seconds')
move_msg = Twist()
move_msg.angular.z = -2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot right for 5 seconds')
move_msg = Twist()
move_msg.linear.x = 1
move_msg.angular.z = 2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot left for 5 seconds')
move_msg = Twist()
move_msg.linear.x = -1
move_msg.angular.z = 2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot right for 5 seconds')
move_msg = Twist()
move_msg.linear.x = 1
move_msg.angular.z = -2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot left for 5 seconds')
move_msg = Twist()
move_msg.linear.x = -1
move_msg.angular.z = -2.0
move.publish(move_msg)
time.sleep(5.0)

print('Turning robot left for 0.5 seconds')
move_msg = Twist()
move_msg.linear.x = 0.0
move_msg.angular.z = 0.0
move.publish(move_msg)
time.sleep(0.5)

