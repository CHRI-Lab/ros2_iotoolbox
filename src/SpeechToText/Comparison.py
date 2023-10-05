import speech_recognition as sr


# Using speech_recognition with Google's free API
def transcribe_with_speech_recognition(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service."


import openai


def audio_to_text(audio_filepath, api_key):
    # Set the OpenAI API key
    openai.api_key = api_key

    # Open the audio file in binary read mode
    with open(audio_filepath, "rb") as audio_file:
        # Translate audio to text using the Whisper API (assuming this is how it's done)
        response = openai.Audio.translate(file=audio_file,
                                          model="whisper-1",
                                          response_format="text",
                                          language="en")

        # Extract transcript from the response (assuming there's a 'data' field with 'transcript' inside)
        transcript = response

    return transcript

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



# Usage
audio_filepath = "sample.wav"
api_key = "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"
transcript = audio_to_text(audio_filepath, api_key)

audio_filepath = "sample.wav"
speech_recognition_transcript = transcribe_with_speech_recognition(audio_filepath)

print("Speech Recognition Transcript:", speech_recognition_transcript)
print("OpenAI Transcript:", transcript)
try:
    text = recognizer.recognize_google(audio_data)
    print("Google Web Speech API Transcript:", text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError:
    print("Google Web Speech API request failed")
