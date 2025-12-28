# main.py

# Apne banaye hue package se "team members" (classes) ko import karna
from tts_package.data_handler import DataHandler
from tts_package.voice_config import VoiceConfig
from tts_package.tts_engine import TTSEngine
import os

# --- DEMO KE LIYE EK DUMMY TXT FILE BANANE KA FUNCTION ---
# Yeh function check karega ki input.txt file hai ya nahi. Agar nahi, to bana dega.
def create_dummy_files():
    """Ek dummy .txt file banata hai taaki program test ho sake."""
    if not os.path.exists("input.txt"):
        print("Dummy file 'input.txt' nahi mili, isliye ek nayi file bana rahe hain...")
        with open("input.txt", "w", encoding="utf-8") as f:
            f.write("This is a test from a text file. Object Oriented Programming makes code clean and reusable.")
    
    # Hum user ko .docx file ke baare mein inform kar denge
    if not os.path.exists("input.docx"):
        print("\nNote: Word file 'input.docx' nahi mili. Aap chahein to ek bana kar test kar sakte hain.")

def main():
    """
    Application ka main function (Director's script).
    """
    print("---=== Professional TTS Application ===---\n")
    create_dummy_files() # Sabse pehle dummy file check/create ki

    # =================================================================
    # --- SCENARIO 1: .txt file se padhna aur Female aawaz mein bolna ---
    # =================================================================
    print("--- SCENARIO 1: Reading from input.txt with a Female Voice ---")
    
    # Step 1: Script writer (DataHandler) ko kaam diya
    handler_txt = DataHandler()
    handler_txt.load_from_txt("input.txt")
    print(f"Shabdon ki ginti (Word Count): {handler_txt.word_count}")

    # Step 2: Casting director (VoiceConfig) se female voice ki settings li
    female_config = VoiceConfig(rate=165, gender='female', volume=0.9)

    # Step 3: Actor (TTSEngine) ko bulaya, settings di, aur dialogue bulwaya
    speaker = TTSEngine(config=female_config)
    print("Ab bolna shuru kar rahe hain...")
    speaker.speak(handler_txt.text_content)
    
    print("\n" + "="*50 + "\n")

    # ======================================================================
    # --- SCENARIO 2: Direct text likhna aur Male aawaz mein file save karna ---
    # ======================================================================
    print("--- SCENARIO 2: Writing text and saving to file with a Male Voice ---")

    # Step 1: Script writer (DataHandler) ko direct dialogue diya
    handler_string = DataHandler()
    direct_text = "This is a direct string input. I will be saved as an audio file with a faster, male voice."
    handler_string.load_from_string(direct_text)
    print(f"Shabdon ki ginti (Word Count): {handler_string.word_count}")

    # Step 2: Casting director (VoiceConfig) se male voice ki settings li
    male_config = VoiceConfig(rate=180, gender='male', volume=1.0)

    # Step 3: Naye Actor (TTSEngine) ko bulaya aur audio file save karne ko kaha
    saver = TTSEngine(config=male_config)
    saver.save_to_file(handler_string.text_content, filename="male_voice_output.mp3")


if __name__ == "__main__":
    # Yeh line सुनिश्चित karti hai ki Director (main function) tabhi kaam kare jab script direct run ho
    main()

