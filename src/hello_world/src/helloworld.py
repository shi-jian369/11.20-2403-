import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('helloworld', anonymous=True)
    pub = rospy.Publisher('abcsdfj', String, queue_size=10)
    rospy.loginfo("Hello, world!")

    rate = rospy.Rate(10)  # 10Hz
    while not rospy.is_shutdown():
        rospy.loginfo("Hello, world!")
        msg = String()
        msg.data = "Hello, ros!"
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
