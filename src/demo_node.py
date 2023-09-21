import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import openai

class TranslateNode(Node):
    def __init__(self):
        super().__init__('translate_node')
        self.publisher_ = self.create_publisher(String, 'translated_sentence', 10)
        self.subscription = self.create_subscription(String, 'input_sentence', self.callback, 10)

        openai.api_key = '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'

    def callback(self, msg):
        sentence = msg.data
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Translate the sentence into action and object, for example a sentence 'move that cup' should be 'Action: move; Object: cup'. Now please translate {sentence}",
            max_tokens=100
        )

        text = response['choices'][0]['text']
        action = text.split("Action: ")[1].split(";")[0].strip()
        obj = text.split("Object: ")[1].strip().replace(".", "")

        self.get_logger().info(f"Action: {action}")
        self.get_logger().info(f"Object: {obj}")
        cost = response['usage']['total_tokens']
        self.get_logger().info(f"Cost would be {cost}")

        translated_msg = String()
        translated_msg.data = f"Action: {action}, Object: {obj}"
        self.publisher_.publish(translated_msg)

def main():
    rclpy.init()
    translate_node = TranslateNode()
    rclpy.spin(translate_node)
    translate_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
