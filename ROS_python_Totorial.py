#Testing for using python beyond the basics of ROS
import rospy
from std_msgs.msg import Int32

int length = 5
int width = 10
int height = 26

def talker():
    length = rospy.publisher('length',Int 32, queue_size = 10)
    width = rosypy.publisher('width',Int 32, queue_size = 10)
    height = rospy.publisher('height',Int 32, queue_size = 10)

    rospy.init_node('Ros_python_Totorial')


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



