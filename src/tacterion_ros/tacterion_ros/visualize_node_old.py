import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

class LivePlotNode(Node):
    def __init__(self):
        super().__init__('live_plot_node')
        self.subscription = self.create_subscription(String, 'sensor_data', self.listener_callback, 10)
        self.data = deque(maxlen=100)

        self.fig, self.ax = plt.subplots()
        self.ani = FuncAnimation(self.fig, self.update_plot, interval=100)
        plt.ion()
        plt.show()

    def listener_callback(self, msg):
        try:
            values = list(map(float, msg.data.split(',')))
            self.data.append(values)
        except ValueError:
            pass

    def update_plot(self, _):
        if not self.data:
            return
        self.ax.clear()
        transposed = list(zip(*self.data))
        for series in transposed:
            self.ax.plot(series)

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
