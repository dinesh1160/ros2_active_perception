import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import threading

class InteractiveTrigger(Node):
    def __init__(self):
        super().__init__('interactive_trigger')
        self.eval_client = self.create_client(Trigger, '/evaluate_now')
        self.finish_client = self.create_client(Trigger, '/finish_benchmark')
        
        # Run the input prompt in a separate thread so it doesn't block ROS 2 spin
        self.input_thread = threading.Thread(target=self.cli_loop, daemon=True)
        self.input_thread.start()

    def cli_loop(self):
        print("\n--- Active Perception Manual Control ---")
        print("Point your camera at the object, then press ENTER to evaluate the angle.")
        print("Type 'exit' and press ENTER to complete the session and print the scoreboard.\n")
        
        while rclpy.ok():
            user_input = input(">> Action (ENTER to score / 'exit' to finish): ").strip().lower()
            
            if user_input == 'exit':
                self.call_service(self.finish_client)
                print("Shutdown command sent. Check the Coordinator terminal for results.")
                rclpy.shutdown()
                break
            elif user_input == '':
                self.call_service(self.eval_client)
            else:
                print("Invalid command. Press ENTER or type 'exit'.")

    def call_service(self, client):
        if not client.wait_for_service(timeout_sec=2.0):
            print("[ERROR] Service not available. Is the Coordinator running?")
            return
        
        req = Trigger.Request()
        future = client.call_async(req)
        # We don't block for the result here; the Coordinator prints to its own terminal.

def main(args=None):
    rclpy.init(args=args)
    node = InteractiveTrigger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
