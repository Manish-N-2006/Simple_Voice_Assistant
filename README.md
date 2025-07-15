# 🤖 V.A.S.P.Y. - Voice-based Assistant for Speech Processing using Python

V.A.S.P.Y. is an intelligent **desktop voice assistant** built entirely in **Python**, designed to respond to voice commands and automate a wide range of desktop and web-based tasks. From opening apps and sending WhatsApp messages to searching YouTube and speaking responses — V.A.S.P.Y. is your personal productivity companion.

> 🚧 **Note:** This application is currently under development with more features to be added.

---

## 🔤 Full Form

**V.A.S.P.Y.** stands for:

> **V**oice-based  
> **A**ssistant for  
> **S**peech  
> **P**rocessing using  
> **Py**thon

---

## 🎯 Features

- 🗣️ Wake-word-based activation (**"Vaspy"** by default)
- 🧠 Speech recognition using Google Speech API (online)
- 🎤 Text-to-speech responses using `pyttsx3` (offline)
- 📂 Open and **close** system apps like Notepad, Calculator, CMD, Paint, etc.
- 🌐 Open websites: YouTube, Google, ChatGPT, Amazon, GitHub, etc.
- 🎵 Search and play YouTube videos using `youtubesearchpython`
- 💬 Send WhatsApp messages via voice using `pywhatkit`
- ⚙️ Open specific Windows settings like Wi-Fi, General settings
- 💡 Modular and easy to extend Python code

---

## 🛠 Tech Stack

| Module                  | Purpose                                 |
|-------------------------|------------------------------------------|
| `speech_recognition`    | Convert voice to text (via Google API)   |
| `pyttsx3`               | Offline text-to-speech                   |
| `pywhatkit`             | WhatsApp messaging, YouTube playback     |
| `webbrowser`            | Open web URLs in browser                 |
| `os`                    | Launch and kill desktop apps             |
| `random`                | Random greetings                        |
| `youtubesearchpython`   | YouTube search integration               |

---

## 📦 Installation

- pip install speechrecognition pyttsx3 pywhatkit youtubesearchpython
  
- ✅ Enable your system microphone and allow Python to use it.

## 🚀 How to Run

- python main.py
- Say **Spy** to activate the assistant.

---

## 💡 Example Commands

Voice Command	Action
- "Vaspy, open notepad"	Launches Notepad
- "Vaspy, close notepad"	Closes Notepad using task manager
- "Vaspy, play Despacito on YouTube"	Opens YouTube and plays result
- "Vaspy, send WhatsApp message"	Starts WhatsApp voice messaging flow

---

## 🔐 Notes

- Uses Google’s API for speech recognition → Internet required
- Works on Windows OS for now (tested)
- Wake word is customizable (default: "Vaspy")

---

## 🧑‍💻 Author

- Manish N
- B.Tech CSE (AI & Python Development)
- GitHub: Manish-N-2006
- Project Repository: Simple_Voice_Assistant
