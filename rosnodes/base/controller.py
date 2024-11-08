'''
Usage :
    Recive the data from the joystick and publish the velocity and buttons

topics :
    /joystick_buttons       : publish
    /joystick_cmd           : publish
'''

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String , Int8MultiArray
from src.joystick import Joystick


class Controller(Node):

    def __init__(self):
        super().__init__("serial_cmd_publisher")
        self.controller = Joystick()

        self.button_publisher = self.create_publisher(Int8MultiArray,"/joystick_buttons",10)
        self.serial_cmd_publisher =  self.create_publisher(String,"/joystick_cmd",10)

        self.timer = self.create_timer(0.5,self.get_values)
    
    def get_values(self):
        buttons = self.get_button()
        cmd     = self.get_cmd()
        self.button_publisher.publish(buttons)
        self.serial_cmd_publisher.publish(cmd)


    def get_button(self):
        buttons = Int8MultiArray()
        buttons.data = self.controller.buttons_data
        return buttons

    def get_cmd(self):
        cmd = String()
        cmd.data = self.controller.cmd
        return cmd

def main():
    rclpy.init(args=None)
    publisher = Controller()
    rclpy.spin(publisher)

if __name__ == '__main__':
    main()

