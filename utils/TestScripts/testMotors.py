#!/usr/bin/env python

import time
import rospy
import roslib

from geometry_msgs.msg import Twist

rospy.init_node("test")

move = rospy.Publisher('cmd_vel', Twist, queue_size=4)

time.sleep(1)

move_msg = Twist()
move_msg.linear.x = 1
move_msg.angular.z = 0.0
move.publish(move_msg)

