# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\Test_ASCII_Art_Studio.py

from PIL import Image
import numpy as np
import unittest

class Test_ASCII_Art_Studio(unittest.TestCase):
    
    def test_load_nonexistent_file(self):
        studio = ASCII_Art_Studio()
        with self.assertRaises(FileNotFoundError):
            studio.load('nonexistent_file.jpg')
    
    def test_load_incorrect_format(self):
        studio = ASCII_Art_Studio()
        with self.assertRaises(ValueError):
            studio.load('incorrect_format.txt')  # Assuming .txt is an invalid format
    
    def test_info_no_image_loaded(self):
        studio = ASCII_Art_Studio()
        with self.assertRaisesRegex(ValueError, "No image loaded"):
            studio.info()
    
    # ... (additional unit tests)

if __name__ == "__main__":
    unittest.main()
