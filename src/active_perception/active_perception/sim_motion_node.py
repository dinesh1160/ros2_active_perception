import time

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_srvs.srv import Trigger
from active_perception_interfaces.srv import CorrectiveMove


class SimMotionNode(Node):
    def __init__(self):
        super().__init__('sim_motion_node')
        self.declare_parameter('move_duration_sec', 1.0)
        self.duration = self.get_parameter('move_duration_sec').value
        self.create_service(Trigger, '/move_to_next_view', self.handle_move)
        self.create_service(CorrectiveMove, '/corrective_move', self.handle_corrective)
        self.get_logger().info("Simulated motion ready (no robot: moves are only logged).")

    def handle_move(self, request, response):
        self.get_logger().info("[sim] orbit step to the next view")
        time.sleep(self.duration)
        response.success = True
        response.message = "simulated orbit step"
        return response

    def handle_corrective(self, request, response):
        self.get_logger().info(
            f"[sim] {request.action} {request.value:+.2f} (radius {request.radius:.2f})")
        time.sleep(self.duration)
        response.success = request.action in ('orbit', 'rotate', 'translate')
        response.message = f"simulated {request.action}" if response.success else \
            f"Unknown action '{request.action}'"
        return response


def main(args=None):
    rclpy.init(args=args)
    node = SimMotionNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
