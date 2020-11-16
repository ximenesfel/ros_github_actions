#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

counter = 0
pub = None

def callback_number(msg):
    global counter
    counter += msg.data
    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)

def callback_rest_counter(req):

    if req.data:
        global counter
        counter = 0
        return True, "Counter has been successfully reset"
    else:
        return False, "Counter has not been reset"

if __name__ == '__main__':
    rospy.init_node("number_counter")
    rospy.loginfo("This node number_counter has been started ...")
    sub = rospy.Subscriber("/number", Int64, callback_number)

    pub = rospy.Publisher("/number_count", Int64, queue_size=10)

    rest_service = rospy.Service("/reset_counter", SetBool, callback_rest_counter)

    rospy.spin()