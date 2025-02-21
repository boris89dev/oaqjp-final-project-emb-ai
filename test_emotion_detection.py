from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_predictor(self):
        # Testing the 'joy' emotion – because who doesn't love joy?
        result_1 = emotion_predictor(emotion_detector("I am glad this happened"))
        self.assertIsNotNone(result_1)  # Make sure the result isn't 'missing in action'
        self.assertIn('joy', result_1)  # Check that joy made an appearance
        self.assertGreater(result_1['joy'], 0)  # Make sure joy is actually feeling good (positive score)

        # Testing the 'anger' emotion – things are getting heated now!
        result_2 = emotion_predictor(emotion_detector("I am really mad about this"))
        self.assertIsNotNone(result_2)  # No anger should be left unchecked
        self.assertIn('anger', result_2)  # Ensure the angry emotion is present
        self.assertGreater(result_2['anger'], 0)  # Don't let that anger simmer down to zero

        # Testing the 'disgust' emotion – because sometimes things just... gross us out
        result_3 = emotion_predictor(emotion_detector("I feel disgusted just hearing about this"))
        self.assertIsNotNone(result_3)  # No room for denial here – disgust is real
        self.assertIn('disgust', result_3)  # Disgust better be included, or it’s not a party
        self.assertGreater(result_3['disgust'], 0)  # Make sure disgust isn't pretending to be a nice feeling

        # Testing the 'sadness' emotion – because we all have our 'sad days'
        result_4 = emotion_predictor(emotion_detector("I am so sad about this"))
        self.assertIsNotNone(result_4)  # Let's not ignore sadness, it's a real thing
        self.assertIn('sadness', result_4)  # Sadness should have its moment of fame
        self.assertGreater(result_4['sadness'], 0)  # We want real tears here, not zero

        # Testing the 'fear' emotion – spooky stuff!
        result_5 = emotion_predictor(emotion_detector("I am really afraid that this will happen"))
        self.assertIsNotNone(result_5)  # Fear should not be a ghost – show up, fear!
        self.assertIn('fear', result_5)  # Check that fear made it to the list of emotions
        self.assertGreater(result_5['fear'], 0)  # Fear should not be a tiny squeak, make it big

unittest.main()
