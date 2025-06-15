import unittest
from emotion_app.emotion_detector import emotion_predictor

class TestEmotionDetector(unittest.TestCase):
    def test_valid_text(self):
        result = emotion_predictor("I am so happy today!")
        self.assertIn("emotion", result)

    def test_empty_text(self):
        result = emotion_predictor("")
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main()
