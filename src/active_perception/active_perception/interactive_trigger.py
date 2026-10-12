import sys
import threading

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_srvs.srv import Trigger


class InteractiveTrigger(Node):
    def __init__(self):
        super().__init__('interactive_trigger')
        self.eval_client = self.create_client(Trigger, '/evaluate_now')
        self.finish_client = self.create_client(Trigger, '/finish_benchmark')
        self.done = False

        if not sys.stdin.isatty():
            self.get_logger().error(
                "No interactive terminal (stdin is not a TTY). Run this node with "
                "'ros2 run active_perception interactive_trigger' in its own terminal.")
            self.done = True
            return

        # Run the input prompt in a separate thread so it doesn't block ROS 2 spin
        self.input_thread = threading.Thread(target=self.cli_loop, daemon=True)
        self.input_thread.start()

    def cli_loop(self):
        print("\n--- Active Perception Manual Control ---")
        print("Point the camera at the object, then press ENTER to evaluate the angle.")
        print("Type 'exit' and press ENTER to complete the session and print the scoreboard.\n")

        while rclpy.ok() and not self.done:
            try:
                user_input = input(">> Action (ENTER to score / 'exit' to finish): ").strip().lower()
            except EOFError:
                user_input = 'exit'

            if user_input == 'exit':
                result = self.call_service(self.finish_client, timeout_sec=10.0)
                if result is not None:
                    print(f"Scoreboard printed in the Coordinator terminal. {result.message}")
                self.done = True
            elif user_input == '':
                result = self.call_service(self.eval_client, timeout_sec=5.0)
                if result is not None:
                    status = 'OK' if result.success else 'REJECTED'
                    print(f"[{status}] {result.message}")
            else:
                print("Invalid command. Press ENTER or type 'exit'.")

    def call_service(self, client, timeout_sec):
        """Call a Trigger service from the input thread; the main thread spins the future."""
        if not client.wait_for_service(timeout_sec=2.0):
            print("[ERROR] Service not available. Is the Coordinator running?")
            return None

        event = threading.Event()
        future = client.call_async(Trigger.Request())
        future.add_done_callback(lambda _: event.set())
        if not event.wait(timeout_sec):
            print("[ERROR] No response from the Coordinator.")
            return None
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = InteractiveTrigger()
    try:
        while rclpy.ok() and not node.done:
            rclpy.spin_once(node, timeout_sec=0.1)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
