import tkinter as tk
import sounddevice as sd
import numpy as np
import wavio
import threading

class Recorder:
    def __init__(self, master):
        self.master = master
        self.master.title("Recorder")

        self.is_recording = False
        self.start_btn = tk.Button(self.master, text="Start Recording", command=self.toggle_recording)
        self.start_btn.pack(pady=20)

        self.samplerate = 44100  # Hertz
        self.channels = 2
        self.filename = "/home/nsc/ros2_workspace/src/voice/test1.wav"  # change the output address
        self.recording_chunks = []

    def toggle_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.start_btn.config(text="Start Recording")
            self.stop()
        else:
            self.is_recording = True
            self.start_btn.config(text="Stop Recording")
            threading.Thread(target=self.record).start()

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

if __name__ == "__main__":
    root = tk.Tk()
    recorder = Recorder(root)
    root.mainloop()


