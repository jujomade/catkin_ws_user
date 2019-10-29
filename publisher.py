#!usr/bin/env python
import rospy
from autominy_msgs.msg import NormalizedSteeringCommand
from autominy_msgs.msg import SpeedCommand

pub = rospy.Publisher('subscriber', ,queue_size=10)

rospy.init_node('publisher', anonymous=True)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
	test_string = "Hi, Im there and its %s" % rospy.get_time()
	rospy.loginfo(test_string)
	pub.publish(test_string)
	rate.sleep()


