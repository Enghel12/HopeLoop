# 🎧 HopeLoop

**HopeLoop** is a lightweight, local-first prototype for a conversational AI assistant named **Hope**.  
It records your voice, transcribes it, sends it to **GPT-4** for a response, converts that response into speech using **ElevenLabs**, and plays it back to you — all in a loop, until you say goodbye.

This project was built as an experiment in real-time, voice-driven AI interactions with a bit of attitude and charm.

---

## 🎯 Purpose of the Project

HopeLoop was originally part of a larger project aiming to create a **real-time, interruptible AI tech support voice agent**.  
While that dream now moves to a WebSocket-based architecture, this local prototype remains as a practice-focused, contained system where you can:

- Record your voice
- Interact with GPT-4 via speech
- Hear AI responses in a natural, human-like voice
- Build your understanding of conversational AI flow using real APIs

---

## 🧰 Tech Stack

| Feature               | Tech Used                 |
|----------------------|---------------------------|
| Voice Recording      | `sounddevice`, `scipy`    |
| Speech-to-Text (STT) | OpenAI Whisper            |
| AI Brain             | OpenAI GPT-4              |
| Text-to-Speech (TTS) | ElevenLabs                |
| Audio Playback       | `playsound`               |
| Secrets Management   | `python-dotenv`           |
| Project Type         | CLI / Local Prototype     |

---

## 🚀 How It Works

1. You speak — Hope listens and records your voice for 5 seconds.
2. Your voice is transcribed using OpenAI’s Whisper model.
3. Hope sends your words to GPT-4, along with the full conversation history.
4. GPT-4 replies (in Hope’s cheerful tone).
5. ElevenLabs converts Hope’s reply into voice.
6. The audio is played back to you using `playsound`.
7. If you say "goodbye", the loop ends. Otherwise, the conversation continues!

---

## 📝 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Enghel12/HopeLoop.git
cd HopeLoop
