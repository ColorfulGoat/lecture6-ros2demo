#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        
        # Create publisher: message type, topic name, queue size
        self.publisher = self.create_publisher(
            Twist,           # Message type
            '/cmd_vel',      # Topic name
            10               # Queue size
        )
        
        # Create timer: publish every 0.5 seconds
        self.timer = self.create_timer(0.5, self.publish_velocity)
        
        self.get_logger().info('Velocity Publisher started! Publishing to /cmd_vel')
    
    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 0.2   # Move forward at 0.2 m/s
        msg.angular.z = 0.5  # Turn left at 0.5 rad/s
        
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    rclpy.spin(node)  # Keep node running
    rclpy.shutdown()

if __name__ == '__main__':
    main()