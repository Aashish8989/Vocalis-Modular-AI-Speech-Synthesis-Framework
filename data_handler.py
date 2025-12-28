# tts_package/data_handler.py

# Word file (.docx) padhne ke liye is library ki zaroorat padegi
# Terminal mein 'pip install python-docx' se install karein
import docx

class DataHandler:
    """
    Yeh class alag-alag sources se text input lene,
    store karne aur word count karne ka kaam karti hai.
    """
    def __init__(self):
        self.text_content = ""
        self.word_count = 0

    def load_from_txt(self, filepath: str):
        """ .txt file se text load karti hai. """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.text_content = f.read()
            self._update_word_count()
            print(f"'{filepath}' se text successfully load ho gaya.")
        except FileNotFoundError:
            print(f"Error: File '{filepath}' nahi mili.")
            self.text_content = ""
            self.word_count = 0

    def load_from_docx(self, filepath: str):
        """ .docx (Word) file se text load karti hai. """
        try:
            doc = docx.Document(filepath)
            full_text = [para.text for para in doc.paragraphs]
            self.text_content = '\n'.join(full_text)
            self._update_word_count()
            print(f"'{filepath}' se text successfully load ho gaya.")
        except Exception as e:
            print(f"Error: Word file '{filepath}' ko padhne mein dikkat: {e}")
            self.text_content = ""
            self.word_count = 0

    def load_from_string(self, input_string: str):
        """ Direct likhe hue text ko load karti hai. """
        self.text_content = input_string
        self._update_word_count()
        print("Direct string se text successfully load ho gaya.")

    def _update_word_count(self):
        """
        Yeh ek private helper method hai jo text_content ke shabdon ko ginta hai.
        """
        if self.text_content:
            words = self.text_content.split()
            self.word_count = len(words)
        else:
            self.word_count = 0
