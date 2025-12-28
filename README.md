**Modular AI Speech Synthesis Engine**

A professional-grade, modular Text-to-Speech (TTS) engine built with Python. This project demonstrates high-level software architecture using Object-Oriented Programming (OOP) principles like Encapsulation, Abstraction, and Single Responsibility.


**🚀 Features**
Multi-Source Data Handling: Seamlessly process text from .txt, .docx, or raw strings.
Modular Architecture: Decoupled components for configuration, data processing, and speech synthesis.
Highly Configurable: Control speech rate, volume, and gender profiles through a dedicated config interface.
Optimized Performance: Lightweight engine initialization with automated word-counting and text processing.


**🛠️ Tech Stack**

Language: Python 3.x
Core Library: pyttsx3
Document Parsing: python-docx
Design Pattern: Object-Oriented Programming (OOP)

**📦 Project Structure**

├── tts_package/            # Core Package
│   ├── __init__.py         # Package marker
│   ├── voice_config.py     # Voice settings & validation logic
│   ├── data_handler.py     # Input processing for txt/docx/strings
│   └── tts_engine.py       # Core synthesis engine (Encapsulated)
├── main.py                 # Application Entry Point
└── requirements.txt        # Project dependencies


**Install dependencies:**

pip install -r requirements.txt


**Run the application:**
python main.py


🧪 OOP Principles Applied

Encapsulation: The internal state of the pyttsx3 engine is hidden within the TTSEngine class, exposing only necessary methods like speak() and save_to_file().
Abstraction: Users interact with simple interfaces for loading data and configuring voices without needing to understand the underlying speech synthesis logic.
Modularity: Every file has a single responsibility, making the system easy to scale and debug.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

**Developed with focus on technical speed and clean code.**
