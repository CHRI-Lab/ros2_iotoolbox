# This is a sample Python script use whisper to translate speech to text.


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
def check_grammar(transcript, api_key):
    # Set the OpenAI API key
    openai.api_key = api_key

    # Send the transcript to ChatGPT with a prompt to check its grammar
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Please correct the grammar of the following text: \"{transcript}\"",
        max_tokens=500
    )

    # Extract the corrected text from the response
    corrected_text = response.choices[0].text.strip()

    return corrected_text

# Usage
audio_filepath = "sample.wav"
api_key = "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"
transcript = audio_to_text(audio_filepath, api_key)
print("Original Transcript:", transcript)

corrected_transcript = check_grammar(transcript, api_key)
print("Corrected Transcript:", corrected_transcript)
