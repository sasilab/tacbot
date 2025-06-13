import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for headless systems

import matplotlib.pyplot as plt
from collections import deque
import time
import os

class LivePlotNode(Node):
    def __init__(self):
        super().__init__('live_plot_node')

        # Subscribes to /sensor_data topic
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10
        )
        self.data = deque(maxlen=100)  # Store last 100 data points

        # Set up the figure for saving
        self.fig, self.ax = plt.subplots()
        
        # Create a timer to save plots every 5 seconds
        self.timer = self.create_timer(5.0, self.save_plot)
        self.get_logger().info("LivePlotNode is running and saving plots...")

    def listener_callback(self, msg):
        try:
            values = list(map(float, msg.data.split(',')))
            self.data.append(values)
        except ValueError:
            self.get_logger().warn("Received malformed data. Skipping.")

    def save_plot(self):
        if not self.data:
            return
        self.ax.clear()
        transposed = list(zip(*self.data))  # Split each column
        for series in transposed:
            self.ax.plot(series)
        
        timestamp = int(time.time())
        filename = f"/root/ros2_ws/plot_{timestamp}.png"
        self.fig.savefig(filename)
        self.get_logger().info(f"Saved plot to {filename}")

def main(args=None):
    rclpy.init(args=args)
    node = LivePlotNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
