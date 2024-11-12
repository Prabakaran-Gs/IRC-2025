import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray


class Controller(Node):

    def __init__(self):
        super().__init__("serial_cmd_reciever")
        
        self.motion_subscriber = self.create_subscription(String,"joystick_motion_cmd",self.motion_writer)
        self.arm_subscriber = self.create_subscription(String,"joystick_arm_cmd",self.arm_writer)

    def arm_writer(self,msg :Float32MultiArray):

        data = list(msg.data)
        # ! float => int implementation
        cmd = " ".join(data)
        # print(cmd)
        # ! Serial write to Arduino cmd
        pass

    def motion_writer(self,msg :String):

        cmd = msg.data
        print(cmd)
        # ! Serial write to Arduino cmd


def main():
    rclpy.init()
    node = Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

    