import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sounddevice as sd
import numpy as np
import wavio
import threading

class RecorderNode(Node):
    def __init__(self):
        super().__init__('recorder_node')

        self.is_recording = False
        self.publisher_ = self.create_publisher(String, 'audio_filepath', 10)

        self.master = master
        self.master.title("Recorder")
        self.master.geometry("800x600")
        
        self.samplerate = 44100  # Hertz
        self.channels = 2
        self.filename = "/home/nsc/ros2_workspace/src/voice/test1.wav"
        self.recording_chunks = []

        self.start_recording_thread = threading.Thread(target=self.record)

    def toggle_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.start_btn.config(text="Start Recording")
            self.stop()
        else:
            self.is_recording = True
            self.start_btn.config(text="Stop Recording")
            self.start_recording_thread.start()

    def record(self):
        with sd.InputStream(samplerate=self.samplerate, channels=self.channels) as stream:
            while self.is_recording:
                audio_chunk, _ = stream.read(self.samplerate)
                self.recording_chunks.append(audio_chunk)

    def stop(self):
        self.is_recording = False
        if self.recording_chunks:
            full_recording = np.vstack(self.recording_chunks)
            wavio.write(self.filename, full_recording, self.samplerate, sampwidth=2)
            self.recording_chunks = []

            audio_filepath_msg = String()
            audio_filepath_msg.data = self.filename
            self.publisher_.publish(audio_filepath_msg)

def main(args=None):
    rclpy.init(args=args)
    recorder_node = RecorderNode()
    rclpy.spin(recorder_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


