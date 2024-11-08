import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from threading import Thread

zed_img_topic ="zed2i/zed_img/left_img_rect"
zed_depth_topic ="zed2i/zed_depth/depth"


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__("image_subscriber")

        #* Stores the image and depth
        self.image = None
        self.depth_img = None
        
        #* Creates 2 subscriber for depth and image
        self.bridge = CvBridge()
        self.image_subscriber = self.create_subscription(Image, zed_img_topic, self.image_callback, 10)
        self.depth_subscriber = self.create_subscription(Image, zed_depth_topic, self.depth_callback, 10)

    def image_callback(self, msg):
        self.image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

    def depth_callback(self, msg):
        self.depth_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding="mono8")

def _spinner(node):
    rclpy.spin(node)


def start_node():
    node = ImageSubscriber()
    thread_obj = Thread(target=_spinner, args=(node,))
    thread_obj.start()
    return node


    