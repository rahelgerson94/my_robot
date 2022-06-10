import rclpy
from rclpy.node import Node
#TODO: import custom message package

from std_msgs.msg import String

#subscribes to HardwareInterface node
class MoveMotor(Node):
    def __init__(self):
        super().__init__('MoveMotor')
        self.subscription = self.create_subscription(
            #TODO: insert custom message type here,
            String,
            'nav/move',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        
def main(args=None):
    rclpy.init(args=args)

    move_motor = MoveMotor()
	
	#spin(): Execute work and block until the context associated with 
	#the executor is shutdown.
    rclpy.spin(move_motor)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    move_motor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
