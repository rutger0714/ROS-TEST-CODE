import rospy
from std_msgs.msg import Int32

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
    rospy.subscriber('length',Int32, length_callback)
    rospy.subscirber('width',Int32,width_callback)
    rospy.subscirber('height',Int32,height_callback)
    int volume = height*width*length
    rospy.init_node('Subscriber_example')
    rospy.publisher('volume', Int32, queue_size = 10)
    
if __name__ == '__main__':
    try:
        listener()
	
    except rospy.ROSInterruptException:
        pass
