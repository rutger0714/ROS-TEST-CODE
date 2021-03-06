#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

length = 5
width = 10
height = 26

def talker():
    global length
    global width
    global height
    length_publish = rospy.Publisher('length',Int32, queue_size = 10)
    width_publish = rospy.Publisher('width',Int32, queue_size = 10)
    height_publish = rospy.Publisher('height',Int32, queue_size = 10)

    rospy.init_node('Ros_python_Totorial')

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        length_publish.publish(length)
        width_publish.publish(width)
        height_publish.publish(height)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



