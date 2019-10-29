#!/usr/bin/env python
import rospy
from autominy_msgs.msg import Speed

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

rospy.init_node('subscriber', anonymous=True)

rospy.Subscriber("/sensors/speed", Speed, callback)

rospy.spin()

