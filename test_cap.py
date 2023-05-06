import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = "hello"
        result = cap.cap_text(text) 
        self.assertEqual(result, "Hello")
        
    def test_multiple_worlds(self):
        text = "hello there!"
        result = cap.cap_text(text)
        self.assertEqual(result, "Hello There!")
        
if __name__ == "__main__":
    unittest.main()