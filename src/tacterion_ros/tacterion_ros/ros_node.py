import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .data_receiver import D01Sensor

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        try:
            self.sensor = D01Sensor()
            self.get_logger().info(f"Connected to sensor on {self.sensor.ser.port}")
        except RuntimeError as e:
            self.get_logger().error(f"Sensor connection failed: {e}")
            raise SystemExit(1)

        self.publisher = self.create_publisher(String, 'sensor_data', 10)
        self.timer = self.create_timer(1.0 / 30.0, self.publish_data)

    def publish_data(self):
        data = self.sensor.read_line()
        if data:
            msg = String()
            msg.data = ','.join(data)
            self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
