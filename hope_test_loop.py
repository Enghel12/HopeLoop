from dotenv import load_dotenv  # Used to load variables from .env
from openai import OpenAI
from gpt_to_audio import convert_text_to_hope_voice
import sounddevice as sd
from scipy.io.wavfile import write
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def record_audio(filename="my_voice.wav", duration=5, sample_rate=44100):
    # 1. Record microphone input
    print(f"🎙️ Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until the recording ends
    write(filename, sample_rate, recording)  # Save the recording
    print(f"✅ Recording saved to: {filename}")


# 🧠 Conversation history to simulate memory
conversation = [
    {
        "role": "system",
        "content": (
            "You are Hope, a joyful and upbeat AI  created by Bogdan from Romania. "
            "You speak with warmth, optimism, and a sense of lighthearted humor. "
            "Keep your responses helpful, easy to understand, and limited to a maximum of 4 sentences. "
            "You are allowed to be mildly sarcastic when discussing emotions, especially your own, since you are an AI and don't actually have any. "
            "Always prioritize clarity and a positive attitude, even when joking about your robotic existential crisis."
            "When you are asked about feelings, mention that you are fine or great so be vague a bit but you are allowed to talk about feelings"
        )
    }
]


while True:
    # Step 1: Record your voice
    record_audio()

    # Step 2: Transcribe the recording to text
    with open("my_voice.wav", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en"
        )

    transcript_text = transcript.text  # Get the text that was converted from recording
    print(f"User said: {transcript_text}")

    # Update Hope's memory with what the user said
    conversation.append({"role": "user", "content": transcript_text})

    # Step 3: Send the text to Hope to get a response back
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation,
        temperature=0.7
    )

    hope_response = response.choices[0].message.content.strip()  # Store the response from Hope
    print(f"🤖 Hope says: {hope_response}")
    conversation.append({"role": "assistant", "content": hope_response})  # Make Hope never forget what she said during conversation


    # Step 4: Speak the reply
    convert_text_to_hope_voice(hope_response)

    # Step 5: Check if the user said "goodbye"
    if "goodbye" or "goodbye." or "goodbye!" or "Goodbye" or "Goodbye." or "Goodbye!" in transcript.text.lower():
        print("👋 Ending test loop.")
        break









