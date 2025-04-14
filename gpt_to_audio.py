import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from playsound import playsound  # ✅ This is all we need for audio playback

# Load environment variables
load_dotenv()

# Set up ElevenLabs client
client = ElevenLabs(api_key=os.getenv("ELEVEN_LABS_API_KEY"))
voice_id = os.getenv("HOPE_VOICE_ID")

def convert_text_to_hope_voice(gpt_response):
    output_path = os.path.abspath("hope_response.mp3")

    # 💣 Safely remove the old file first
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
            print("🧹 Removed old hope_response.mp3")
        except PermissionError:
            print("🚫 File is in use. Try closing your media player.")
            return

    # 🎤 Generate new audio using Eleven Labs api
    audio_generator = client.text_to_speech.convert(
        text=gpt_response,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )

    with open(output_path, "wb") as f:
        for chunk in audio_generator:
            f.write(chunk)

    print(f"🔊 Hope's voice saved to: {output_path}")

    # 🎧 Play audio (BLOCKING)
    playsound(output_path)
