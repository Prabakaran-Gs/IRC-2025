'''
Usage :
    Recive the data from the joystick and publish the velocity and buttons

topics :
    /joystick_buttons       : publish
    /joystick_cmd           : publish
'''

import rclpy
from rclpy.node import Node
from std_msgs.msg import String ,Float32MultiArray
from joystick import Joystick
from config.get_configuration import configuration

NO_OF_BUTTONS_TO_SHARE = configuration.get("BUTTONS_FOR_ARM",8)
motion_topic = configuration.get("ROVER_CONTROL")
arm_topic = configuration.get("ARM_CONTROL")

class Controller(Node):

    def __init__(self):
        super().__init__("serial_cmd_sender")
        self.controller = Joystick()

        self.motion_cmd_publisher =  self.create_publisher(String,motion_topic,10)
        self.arm_cmd_publisher = self.create_publisher(Float32MultiArray,arm_topic,10)
        self.timer = self.create_timer(0.1,self.get_values)
    
    def get_values(self):
        motion     = self.get_motion()
        arm        = self.get_arm()
        self.motion_cmd_publisher.publish(motion)
        self.arm_cmd_publisher.publish(arm)

    def get_arm(self):
        buttons = Float32MultiArray()
        buttons.data = self.controller.axes_data+self.controller.buttons_data[:NO_OF_BUTTONS_TO_SHARE]
        print(buttons)
        return buttons

    def get_motion(self):
        cmd = String()
        cmd.data = self.controller.cmd
        return cmd

def main():
    rclpy.init(args=None)
    publisher = Controller()
    rclpy.spin(publisher)

if __name__ == '__main__':
    main()

