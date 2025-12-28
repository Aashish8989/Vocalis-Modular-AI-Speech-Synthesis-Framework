**Modular AI Speech Synthesis Engine**

A professional-grade, modular Text-to-Speech (TTS) engine built with Python. This project demonstrates high-level software architecture using Object-Oriented Programming (OOP) principles to create a clean, reusable, and "shippable" codebase.

🚀 Features

Multi-Source Data Handling: Seamlessly process text from .txt, .docx, or raw strings.
Decoupled Architecture: Separate components for configuration, data management, and speech synthesis
Configurable Voice Profiles: Easily switch between male/female voices, adjust speech rate, and modify volume.
Automated Processing: Built-in word counting and text splitting logic.

🛠️ Tech Stack

Language: Python 3.x
Core Library: pyttsx3
Document Parsing: python-docx
Design Pattern: Object-Oriented Programming (OOP)

📖 How to Use (Quick Start)

To see the engine in action, follow these simple steps:
Prepare your Input: Create a file named input.txt in the root directory of the project.
Add Content: Type or paste the text you want the AI to speak into input.txt and Save the file.
Run the Application: Execute the main script via terminal:

Bash
python main.py

Listen & Verify:
The engine will immediately read the text aloud using the configured voice.
A high-quality audio file (mp3) will be automatically generated in your folder.

📦 Project Structure
Plaintext

├── tts_package/            # Core Package logic
│   ├── __init__.py         # Package marker
│   ├── voice_config.py     # Voice settings & validation
│   ├── data_handler.py     # Input processing (txt/docx/strings)
│   └── tts_engine.py       # Core synthesis engine (Encapsulated)
├── main.py                 # Application Entry Point (Orchestrator)
├── input.txt               # Your text input file
└── requirements.txt        # Project dependencies

🧪 OOP Principles Applied
Encapsulation: Internal pyttsx3 engine states are protected within the TTSEngine class.
Abstraction: Complex speech synthesis is simplified into high-level speak() and save_to_file() methods
Modularity: Decoupled classes allow for easy scaling.
Developed with a focus on clean architecture and technical speed.
