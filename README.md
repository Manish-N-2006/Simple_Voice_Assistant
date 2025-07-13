# 🤖 V.A.S.P.Y. - Voice-based Assistant for Speech Processing using Python

V.A.S.P.Y. is an intelligent **desktop voice assistant** built entirely in **Python**, designed to respond to voice commands and automate a wide range of desktop and web-based tasks. From opening apps and sending WhatsApp messages to searching YouTube and speaking responses — V.A.S.P.Y. is your personal productivity companion.

> 🚧 **Note:** This application is currently under development. 

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

- 🔊 Wake-word-based activation ("Jack" in current version)
- 🧠 Speech recognition using Google Speech API
- 🗣 Text-to-speech response using `pyttsx3`
- 📂 Open and close system apps like Notepad, Calculator, CMD, etc.
- 🌐 Open websites like YouTube, Google, ChatGPT, Amazon, GitHub, etc.
- 🎵 Search and play YouTube videos by voice using `youtubesearchpython`
- 💬 Send WhatsApp messages via voice using `pywhatkit`
- ⚙️ Open Windows settings (Wi-Fi, general settings)
- 📌 Modular code for easy feature expansion

---

## 🛠 Tech Stack

| Module              | Purpose                               |
|---------------------|----------------------------------------|
| `speech_recognition`| Convert voice input to text (online)   |
| `pyttsx3`           | Text-to-speech synthesis (offline)     |
| `pywhatkit`         | WhatsApp messaging + YouTube playback  |
| `webbrowser`        | Open URLs in default browser           |
| `os`                | App launching & system control         |
| `random`            | Randomized greeting responses          |
| `youtubesearchpython` | YouTube search and link extraction   |

---

## 🖥 Requirements

Install the required packages using pip:

pip install speechrecognition pyttsx3 pywhatkit youtubesearchpython

✅ Note: Ensure your microphone is enabled and Python is installed.

---

## 🚀 How to Run

- python main.py

- Say "Vaspy" to activate the assistant, then give your voice command.

---

## 🔐 Notes
- Uses Google Speech API for voice-to-text (internet required).
- Text-to-speech and app management works offline.
- Assistant currently responds to the wake word "Vaspy" — customizable.

---

## 🔄 Upcoming Features

- ✅ Wake word training customization
- ✅ GUI version using Tkinter or CustomTkinter
- ✅ Background run mode with tray minimization

---

## 🧠 Project Status

- 📌 This is an educational and experimental project.

---

🧑‍💻 Author
Manish N
B.Tech CSE with a focus on AI & Python development
GitHub: Manish-N-2006
