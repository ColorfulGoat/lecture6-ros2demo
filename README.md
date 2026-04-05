# Lecture 6: ROS 2 Concepts & Building Software Packages
## Name: Iason Katsikis, ID: 25-119-710, ROS2 version: Humble
- ### Aufgabe 1,a)
>Terminal Screenshot of package structure

![Terminal Screenshot](/images/Screenshot2.png)

> Python code: circle_motion.py

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleMotion(Node):
    def __init__(self):
        super().__init__('circle_motion')
        
        # Create publisher: message type, topic name, queue size
        self.publisher = self.create_publisher(
            Twist,           # Message type
            '/cmd_vel',      # Topic name
            10               # Queue size
        )
        
        # Create timer: publish every 0.1 seconds
        self.timer = self.create_timer(0.1, self.publish_velocity)
        
        self.get_logger().info('Circle Motion started!')
    
    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 0.3   # Move forward at 0.3 m/s
        msg.angular.z = 0.5  # Turn left at 0.5 rad/s
        
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = CircleMotion()
    rclpy.spin(node)  # Keep node running
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
>Robot moving in circles

| Robot motion | in circles |
|--------|---------|
| ![i1](/images/Screenshot7.png) | ![i2](/images/Screenshot6.png) |
| ![i3](/images/Screenshot9.png) | ![i4](/images/Screenshot5.png) |

>Explain: Why use create_timer()?
>-------------
>We use create_timer because we want to ensure that the velocity commands are published every 0.1 seconds (10Hz). Without it, the publishing speed would depend on the CPU load, making it unstable.

- ### Aufgabe 1,b)
> Python code: odom_monitor.py

``` python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomMonitor(Node):
    def __init__(self):
        super().__init__('odom_monitor')
        
        # Create subscriber: message type, topic name, callback function, queue size
        self.subscription = self.create_subscription(
            Odometry,               # Message type
            '/odom',                # Topic name
            self.odometry_callback, # Callback function
            10                      # Queue size
        )
        
        self.get_logger().info('Odometry Monitor started!')
    
    def odometry_callback(self, msg):
        # Extract position
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        
        # Extract linear velocity
        vx = msg.twist.twist.linear.x
        vz = msg.twist.twist.angular.z
        
        self.get_logger().info(
            f'Position: x={x:.2f}, y={y:.2f} | Velocity: vx={vx:.2f}, vz={vz:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdomMonitor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
> Screenshot: Both nodes running (*circle_motion on* **2nd terminal** and *odom_monitor* on **3rd terminal**)

![i5](/images/Screenshot10.png)

> Screenshot: **ros2 node list**

![i6](/images/Screenshot11.png)

> Explain: How does pub-sub decoupling work? (3 sentences)
> --------
> Publishers and subscribers only communicate through topics. They are "isolated" from one another, which is why they can be started or stopped independently without affecting the rest of the system.

- ### Aufgabe 2,a)
> Screenshot: **ros2 topic list**

![i7](/images/Screenshot12.png)

> Screenshot: **ros2 topic info /cmd_vel**

![i8](/images/Screenshot13.png)

> Screenshot: **ros2 topic hz /odom**

![i9](/images/Screenshot14.png)

> Screenshot: **ros2 node list**

![i10](/images/Screenshot15.png)


