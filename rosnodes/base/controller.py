'''
Usage :
    Recive the data from the joystick and publish the velocity and buttons

topics :
    /cmd_vel       : publish
    /action_button : publish
'''

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
from src.joystick import Joystick


class Controller(Node):

    def __init__(self):
        super().__init__("controller")
        self.controller = Joystick()
        self.velocity_publisher = self.create_publisher(Twist,"/cmd_vel",10)
        self.button_publisher = self.create_publisher(Int8,"/action_button",10)
        self.callback = self.create_timer(0.5,self.get_values)
    
    def get_values(self):
        _direction = self.controller.direction
        _button = self.controller.button

        movement =Twist()
        button = Int8()

        if _direction == 'F':
            movement.linear.x = self.controller.speed
        elif _direction == 'B':
            movement.linear.x = -1* self.controller.speed
        elif _direction == 'L':
            movement.angular.z = -1* self.controller.speed
        elif _direction == 'R':
            movement.angular.z = self.controller.speed

        button.data = _button
        
        self.button_publisher.publish(button)
        self.velocity_publisher.publish(movement)


def main():
    rclpy.init(args=None)
    publisher = Controller()
    rclpy.spin(publisher)

if __name__ == '__main__':
    main()

