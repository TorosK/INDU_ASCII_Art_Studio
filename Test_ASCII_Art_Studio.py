# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\Test_ASCII_Art_Studio.py

from PIL import Image
import numpy as np
import unittest
from unittest.mock import patch, MagicMock

### -------------------- TESTING --------------------- ###

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
    
    def test_get_ascii_char(self):
        studio = ASCII_Art_Studio()
        # Testing boundary conditions for grayscale values
        self.assertEqual(studio._get_ascii_char(0), ASCII_CHARS[0])  # Should map to the darkest char
        self.assertEqual(studio._get_ascii_char(255), ASCII_CHARS[-1])  # Should map to the lightest char

    def test_adjust_dimensions(self):
        studio = ASCII_Art_Studio()
        # Create a mock image with known dimensions
        mock_image = Image.new('L', (100, 200))
        # Call the _adjust_dimensions method
        adjusted_image = studio._adjust_dimensions(mock_image)
        # Check if the width is 50 as expected
        self.assertEqual(adjusted_image.size[0], 50)
        # Check if the height is adjusted to maintain aspect ratio
        expected_height = int((200 / 100) * 50 * 0.55)  # Aspect ratio calculation
        self.assertEqual(adjusted_image.size[1], expected_height)

    @patch('PIL.Image.open')
    def test_render(self, mock_open):
        # Mock the image and its methods
        mock_image = MagicMock()
        mock_image.convert.return_value = mock_image
        mock_image.size = (100, 100)
        mock_image.getpixel.return_value = 0  # Let's assume all pixels are black for simplicity
        mock_open.return_value.__enter__.return_value = mock_image
        
        studio = ASCII_Art_Studio()
        studio.load('mock_image.jpg')  # We're using a mock object, so the file doesn't need to exist
        ascii_art = studio.render()
        
        # We expect 50 lines of ASCII art, each with 50 characters of the darkest ASCII character
        expected_ascii = "\n".join([ASCII_CHARS[0] * 50 for _ in range(50)])
        self.assertEqual(ascii_art, expected_ascii)

if __name__ == "__main__":
    unittest.main()
