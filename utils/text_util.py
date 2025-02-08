import easyocr

class TextProcessor:
    def __init__(self, source_langs=['en', 'es', 'fr']):
        self.reader = easyocr.Reader(source_langs)
    
    def detect_text(self, frame):
        results = self.reader.readtext(frame)
        return [
            {
                "text": text,
                "position": [tuple(map(int, coord)) for coord in bbox],
                "confidence": confidence
            } for (bbox, text, confidence) in results
        ]