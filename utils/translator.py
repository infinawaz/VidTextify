from transformers import MarianMTModel, MarianTokenizer

class Translator:
    def __init__(self, target_lang='es'):
        # for english
        self.model_name = f'Helsinki-NLP/opus-mt-en-{target_lang}'
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)
    
    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        return self.tokenizer.decode(translated[0], skip_special_tokens=True)