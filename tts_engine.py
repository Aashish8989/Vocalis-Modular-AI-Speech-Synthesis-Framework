# tts_package/tts_engine.py

import pyttsx3
from .voice_config import VoiceConfig

class TTSEngine:
    """
    Yeh hamari main class hai jo pyttsx3 engine ko control karti hai,
    configuration apply karti hai, aur bolti hai.
    """
    def __init__(self, config: VoiceConfig):
        """
        Constructor - TTS engine ko shuru karta hai aur di gayi configuration apply karta hai.
        """
        try:
            self._engine = pyttsx3.init()
            self.config = config
            self._apply_config()
        except Exception as e:
            print(f"Engine shuru karne mein error: {e}")
            self._engine = None

    def _apply_config(self):
        """ Private method jo config object se settings engine par apply karta hai. """
        if not self._engine:
            return

        self._engine.setProperty('rate', self.config.rate)
        self._engine.setProperty('volume', self.config.volume)
        
        voices = self._engine.getProperty('voices')
        for voice in voices:
            if self.config.gender in str(voice.gender).lower():
                self._engine.setProperty('voice', voice.id)
                break

    def speak(self, text: str):
        """ Diye gaye text ko bolta hai. """
        if self._engine and text:
            self._engine.say(text)
            self._engine.runAndWait()
        elif not text:
            print("Bolne ke liye koi text nahi hai.")

    def save_to_file(self, text: str, filename: str = "output.mp3"):
        """ Diye gaye text ko ek audio file mein save karta hai. """
        if self._engine and text:
            self._engine.save_to_file(text, filename)
            self._engine.runAndWait()
            print(f"Audio safaltapoorvak '{filename}' mein save ho gayi hai.")
        elif not text:
            print("Save karne ke liye koi text nahi hai.")
