#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32


def volume_callback(data):
    global volume
    print("The Calculated Volume is")
    volume = data.data
    print(volume)


def listener():
    rospy.Subscriber('volume',Int32, volume_callback )
    rospy.init_node('Subscriber_2.py')
    rospy.spin()



if __name__ == '__main__':
    try:
        listener()
	
    except rospy.ROSInterruptException:
        pass