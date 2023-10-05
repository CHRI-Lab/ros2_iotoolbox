import speech_recognition as sr
from pydub import AudioSegment

# Load the audio file using pydub
audio_segment = AudioSegment.from_wav("sample.wav")

# Convert pydub AudioSegment to raw data bytes
raw_data = audio_segment.raw_data

# Set up the recognizer
recognizer = sr.Recognizer()

# Convert raw data bytes to audio data for SpeechRecognition
audio_data = sr.AudioData(raw_data, audio_segment.frame_rate, audio_segment.sample_width)

# Recognize the audio using Google Web Speech API (requires internet connection)
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcript:", text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError:
    print("Google Web Speech API request failed")

