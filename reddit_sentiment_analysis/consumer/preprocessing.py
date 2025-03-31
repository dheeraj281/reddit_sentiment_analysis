import re

class PreProcessor:
    def __init__(self):
        pass

    @staticmethod
    def clean_text(text):
        """Clean text by removing URLs and special characters."""
        text = re.sub(r'http\S+', '', text)  # Remove URLs
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters
        return text.strip()