# tts_package/voice_config.py

class VoiceConfig:
    """
    Yeh class aawaz ki configuration (settings) ko store karti hai.
    Jaise ki rate, volume, aur gender.
    """
    def __init__(self, rate: int = 170, volume: float = 1.0, gender: str = 'female'):
        """
        Constructor - VoiceConfig ka object banate waqt yeh default values set ho jayengi.

        Args:
            rate (int): Bolne ki speed (words per minute). Default is 170.
            volume (float): Aawaz ka volume (0.0 se 1.0 tak). Default is 1.0.
            gender (str): Aawaz ka gender ('male' ya 'female'). Default is 'female'.
        """
        # Input validation taaki galat value na daali ja sake
        if not (0.0 <= volume <= 1.0):
            raise ValueError("Volume 0.0 aur 1.0 ke beech hona chahiye.")
        if gender.lower() not in ['male', 'female']:
            raise ValueError("Gender sirf 'male' ya 'female' ho sakta hai.")

        self.rate = rate
        self.volume = volume
        self.gender = gender.lower()
