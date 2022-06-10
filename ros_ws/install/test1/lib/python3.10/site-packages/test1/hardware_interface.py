import rclpy
from rclpy.node import Node
import pyserial 
#TODO: import custom message package
from std_msgs.msg import String

class HardwareInterface(Node):

	def __init__(self):
		super().__init__('HardwareInterface')
		#create_publisher declares that the node publishes messages of 
		#type String (imported from the std_msgs.msg module)
		#over a topic named topic, and that the “queue size” is 10
		self.publisher_ = self.create_publisher(String, 'HardwareInterface', 10)
		timer_period = 0.5  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		
	def timer_callback(self):
        #TODO
        '''
        instantiate your message type here?
        monitor serial
        message parser fct
        publish message
        '''
        msg = String()
        #monitor the serial port
        if ser.in_waiting > 0:
            msg.data = ser.readline().decode('utf-8').rstrip()
        self.publisher_.publish(msg)
        #get_logger().info publishes to console
        self.get_logger().info('Publishing: "%s"' % msg.data) 

def main(args=None):
    rclpy.init(args=args)

    hardware_interface = HardwareInterface()

    rclpy.spin(hardware_interface)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    hardware_interface.destroy_node()
    rclpy.shutdown()
       
if __name__ == '__main__':
    main()
