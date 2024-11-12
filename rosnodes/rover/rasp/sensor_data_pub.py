import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import serial


serial_port = "/dev/ttyUSB0"
baudrate = 9600
ser = serial.Serial(serial_port, baudrate) 

class Sensor_Data(Node):

    def __init__(self):
        super().__init__("sensor_reciever")
        self.sensor_publisher = self.create_publisher(Float32MultiArray,"sensor_data",10)
        self.timer_callback = self.create_timer(0.1,self.get_data)

    def get_data(self):
        ser.reset_input_buffer()
        serial_data = ser.readline().decode('utf-8').strip()
        sensor_data = serial_data.split()
        msg = Float32MultiArray()
        msg.data = sensor_data
        self.sensor_publisher.publish(msg)

def main():
    rclpy.init()
    node = Sensor_Data()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()