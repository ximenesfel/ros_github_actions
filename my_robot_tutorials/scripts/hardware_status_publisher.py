#!/usr/bin/env python

import rospy
from my_robot_msgs.msg import HardwareStatus

if __name__ == '__main__':

    rospy.init_node('hardware_status_publisher')
    rospy.loginfo("This node hardware_status_publisher has been started ...")

    pub = rospy.Publisher("/my_robot/hardware_status", HardwareStatus, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_up = True
        msg.debug_messages = "Everthing is running well"
        pub.publish(msg)
        rate.sleep()