#include <ros/ros.h>
#include <std_msgs/String.h>
int main(int argc, char **argv)
{
  ros::init(argc, argv, "helloworld");
  printf("Hello, world!\n");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<std_msgs::String>("abcsdfj", 10);
  while(ros::ok())
  {
    printf("Hello, world!\n");
    std_msgs::String msg;
    msg.data = "Hello,ros!";
    pub.publish(msg);
  }
  return 0;
}