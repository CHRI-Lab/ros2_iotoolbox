import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk
import sounddevice as sd
import numpy as np
import wavio
import threading

class RecorderNode(Node):
    def __init__(self):
        super().__init__('recorder_node')

        # GUI setup
        self.master = tk.Tk()
        self.master.title("Recorder")
        self.master.geometry("400x200")  # Adjust the size as needed

        self.start_btn = tk.Button(self.master, text="Start Recording", command=self.toggle_recording, height=3, width=20)
        self.start_btn.pack(pady=20)
        self.master.bind('<KeyPress-space>', lambda event: self.toggle_recording())
        self.master.bind('<KeyRelease-space>', lambda event: self.toggle_recording())

        # Recording setup
        self.is_recording = False
        self.samplerate = 44100  # Hertz
        self.channels = 2
        self.filename = "/home/nsc/ros2_workspace/src/voice/test1.wav"
        self.recording_chunks = []

        # ROS2 Publisher setup
        self.publisher_ = self.create_publisher(String, 'audio_filepath', 10)

        # New attribute for tracking space key state
        self.space_pressed = False

        # Modify the key bindings in the RecorderNode's __init__ method:
        self.master.bind('<KeyPress-space>', self.handle_space_press)
        self.master.bind('<KeyRelease-space>', self.handle_space_release)

        self.delay_stop_id = None

    def toggle_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.start_btn.config(text="Start Recording")
        else:
            self.is_recording = True
            self.start_btn.config(text="Stop Recording")
            threading.Thread(target=self.record).start()
            
    def handle_space_press(self, event):
        if not self.space_pressed:  # Only start recording on the first press
            self.space_pressed = True
            self.start_recording()
            if self.delay_stop_id:  # If there's a delayed stop pending, cancel it
                self.master.after_cancel(self.delay_stop_id)
                self.delay_stop_id = None

    def handle_space_release(self, event):
        # Delay the stop recording by 100ms to check for subsequent presses
        self.delay_stop_id = self.master.after(100, self.delayed_stop_recording)

    def delayed_stop_recording(self):
        if not self.space_pressed:  # If space is still not pressed after the delay, stop recording
            self.stop_recording()

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.start_btn.config(text="Stop Recording")
            threading.Thread(target=self.record).start()

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.start_btn.config(text="Start Recording")

    
    def record(self):
        with sd.InputStream(samplerate=self.samplerate, channels=self.channels) as stream:
            while self.is_recording:
                audio_chunk, _ = stream.read(self.samplerate)
                self.recording_chunks.append(audio_chunk)
            full_recording = np.vstack(self.recording_chunks)
            wavio.write(self.filename, full_recording, self.samplerate, sampwidth=2)
            self.recording_chunks = []

            # Publish the audio file path
            audio_filepath_msg = String()
            audio_filepath_msg.data = self.filename
            self.publisher_.publish(audio_filepath_msg)

def main(args=None):
    rclpy.init(args=args)
    recorder_node = RecorderNode()
    
    # Integrate ROS2 with the Tkinter loop
    def update():
        rclpy.spin_once(recorder_node, timeout_sec=0.1)
        recorder_node.master.after(100, update)

    update()
    recorder_node.master.mainloop()
    recorder_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()





