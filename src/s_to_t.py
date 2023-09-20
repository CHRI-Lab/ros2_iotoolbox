import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import openai


class VoiceToTextGrammarNode(Node):

    def __init__(self):
        super().__init__('voice_to_text_grammar_node')

        # Publisher to send out the corrected text
        self.publisher_ = self.create_publisher(String, 'input_sentence', 10)

        # Subscription to listen for audio file paths
        self.subscription = self.create_subscription(
            String,
            'audio_filepath',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # OpenAI API key
        self.api_key = "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"  # Replace with your API key

    def listener_callback(self, msg):
        """Callback function for when an audio file path is received."""

        # Extract the audio file path from the received message
        audio_filepath = msg.data

        # Convert the audio to text
        transcript = self.audio_to_text(audio_filepath, self.api_key)
        self.get_logger().info(f'Original Transcript: {transcript}')

        # Check and correct the grammar of the transcript
        corrected_transcript = self.check_grammar(transcript, self.api_key)
        self.get_logger().info(f'Corrected Transcript: {corrected_transcript}')

        # Publish the corrected transcript
        msg = String()
        msg.data = corrected_transcript
        self.publisher_.publish(msg)

    def audio_to_text(self, audio_filepath, api_key):
        """Converts audio to text using the Whisper API."""

        # Set the API key
        openai.api_key = api_key

        # Read the audio file and send it to the Whisper API for conversion
        with open(audio_filepath, "rb") as audio_file:
            response = openai.Audio.translate(file=audio_file,
                                              model="whisper-1",
                                              response_format="text",
                                              language="en")
            transcript = response
        return transcript

    def check_grammar(self, transcript, api_key):
        """Checks and corrects the grammar of the given transcript using ChatGPT."""

        # Set the API key
        openai.api_key = api_key

        # Send the transcript to ChatGPT for grammar correction
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Please correct the grammar of the following text: \"{transcript}\"",
            max_tokens=500
        )
        corrected_text = response.choices[0].text.strip()
        return corrected_text


def main(args=None):
    """Main function to initialize and run the ROS2 node."""

    # Initialize ROS2
    rclpy.init(args=args)

    # Create and run the node
    voice_to_text_grammar_node = VoiceToTextGrammarNode()
    rclpy.spin(voice_to_text_grammar_node)

    # Cleanup
    voice_to_text_grammar_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
