#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
length = 0
width = 0
height = 0
def length_callback(data):
    global length
    print("Given Length ")
    length = data.data
    print(length)

def width_callback(data):
    global width
    print("Given Width ")
    width = data.data
    print(width)

def height_callback(data):
    global height
    print ("Given height ")
    height = data.data
    print(height)



def listener():
    global length
    global width
    global height
    volume = height*width*length
    volume_publish = rospy.Publisher('volume', Int32, queue_size = 10)
    rospy.init_node('Subscriber_example')
    rospy.Subscriber('length',Int32, length_callback)
    rospy.Subscriber('width',Int32,width_callback)
    rospy.Subscriber('height',Int32,height_callback)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        volume_publish.publish(volume)
        rate.sleep() 
    
if __name__ == '__main__':
    try:
        listener()
	
    except rospy.ROSInterruptException:
        pass
