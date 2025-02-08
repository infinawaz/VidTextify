import cv2
import numpy as np
from utils.text_utils import TextProcessor
from utils.translator import Translator

def main():
    # Initialize components
    text_processor = TextProcessor()
    translator = Translator(target_lang='fr')  # Change to your target language
    
    # For YouTube videos: replace with YouTube URL (requires extra setup)
    cap = cv2.VideoCapture('sample_videos/test.mp4')
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break