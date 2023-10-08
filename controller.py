# %%
#!/usr/bin/env python
import sys
import os
import time
os.sys.path.append("DynamixelSDK")
import rclpy
from rclpy.node import Node
import DynamixelSDK
from dynamixel_sdk_custom_interfaces.msg import SetPosition
from dynamixel_sdk_custom_interfaces.srv import GetPosition
# %%
class Motor_Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(SetPosition, '/set_position', 10)
    # def move(self, id_num, pos_num,args=None):
    #     rclpy.init(args=args)
    #     msg=SetPosition(id=id_num,position=pos_num)
    #     Motor_Publisher.publisher_.publish(msg)
class Motor_Client(Node):
    def __init__(self):
        super().__init__('motor_client')
        self.cli = self.create_client(GetPosition, '/get_position')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetPosition.Request()

    def send_request(self, id_num):
        self.req.id = id_num
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()     
class Run:
    def __init__(self,args=None):
        self.args=args
        rclpy.init(args=args)
        self.motor_publisher=Motor_Publisher()
        self.client=Motor_Client()
    def pub_motor(self, id_num, pos_value):
        self.id_num=id_num
        self.pos_value=pos_value
        motor_publisher =self.motor_publisher
        msg=SetPosition(id=id_num,position=pos_value)
        motor_publisher.publisher_.publish(msg)
    def sub_motor(self, id_num):
        self.id_num=id_num
        client = self.client
        response = client.send_request(11)
        print(response)
    def off(self):
        motor_publisher=self.motor_publisher
        motor_publisher.destroy_node()
        rclpy.shutdown()

        
    
#ros2 topic pub -1 /set_position dynamixel_sdk_custom_interfaces/SetPosition "{id:1, position:1000}"
#(home_pose: 2048, 1262, 2426, 2550, 1233)
#(zero_pose: 2048, 2048, 2048, 2048, 2048)

def main(args=None):
    # rclpy.init(args=args)
    id=[11,12,13,14,15]
    home_pos=[2048, 1262, 2426, 2550, 1233]
    zero_pos=[2048, 2048, 2048, 2048, 2048]
    run=Run()
    for i in range(0,5):
        run.pub_motor(id_num=id[i],pos_value=home_pos[i])
    time.sleep(1)
    for i in range(0,5):
        run.pub_motor(id_num=id[i],pos_value=zero_pos[i])

    run.off()


if __name__ == '__main__':
    main()