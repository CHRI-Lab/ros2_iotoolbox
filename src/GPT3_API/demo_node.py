import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import argparse
import openai
# 监听input_sentence话题上的输入句子，然后将翻译后的结果发布到translated_sentence话题上
class TranslateNode(Node):
    def __init__(self):
        super().__init__('translate_node')
        self.publisher_ = self.create_publisher(String, 'translated_sentence', 10)
        self.subscription = self.create_subscription(String, 'input_sentence', self.callback, 10)
        self.subscription 

        parser = argparse.ArgumentParser(description='Translate a sentence into action and object.')
        parser.add_argument('sentence', type=str, help='The sentence to translate.')
        args = parser.parse_args()
        sentence = args.sentence

        openai.api_key = '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'

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Translate the sentence into action and object, for example a sentence 'move that cup' should be 'Action: move; Object: cup'. Now please translate " + sentence,
            max_tokens=100
        )

        text = response['choices'][0]['text']

        action = text.split("Action: ")[1].split(";")[0].strip()
        obj = text.split("Object: ")[1].strip()
        objf = obj.replace(".", "")

        self.get_logger().info("Action: " + action)
        self.get_logger().info("Object: " + objf)
        cost = response['usage']['total_tokens']
        self.get_logger().info("Cost would be " + str(cost))

        translated_msg = String()
        translated_msg.data = f"Action: {action}, Object: {objf}"
        self.publisher_.publish(translated_msg)

def main(args=None):
    rclpy.init(args=args)
    translate_node = TranslateNode()
    rclpy.spin(translate_node)
    translate_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
