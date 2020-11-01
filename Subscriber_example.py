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

volume = height*width*length

def listener():
    volume_publish = rospy.Publisher('volume', Int32, queue_size = 10)
    rospy.init_node('Subscriber_example')
    rospy.Subscriber('length',Int32, length_callback)
    rospy.Subscriber('width',Int32,width_callback)
    rospy.Subscriber('height',Int32,height_callback)
    
rate = rospy.Rate(10)

while not rospy.is_shutdown():

    volume_publish.publish()
    rate.sleep() 
    
if __name__ == '__main__':
    try:
        listener()
	
    except rospy.ROSInterruptException:
        pass
