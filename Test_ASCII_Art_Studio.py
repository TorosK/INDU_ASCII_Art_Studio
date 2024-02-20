# Test_ASCII_Art_Studio.py

import unittest
from ASCII_Art_Studio import ASCII_Art_Studio
from PIL import Image

class Test_ASCII_Art_Studio(unittest.TestCase):
    def setUp(self):
        """Set up an instance of ASCII_Art_Studio before each test."""
        self.studio = ASCII_Art_Studio()

    def test_load_nonexistent_file(self):
        """Test loading a file that does not exist."""
        response = self.studio.load('nonexistent.jpg')
        self.assertEqual(response, "The specified file was not found.")

    def test_load_invalid_file(self):
        """Test loading a file that is not an image."""
        # Assuming 'invalid.txt' is a text file, not an image
        response = self.studio.load('invalid.txt')
        self.assertEqual(response, "The specified file was not found.")

    def test_info_no_image_loaded(self):
        """Test the info method when no image is loaded."""
        response = self.studio.info()
        self.assertEqual(response, "No image loaded")

    # Note: Testing methods that require loading a real image file, such as _resize_image,
    # _convert_to_ascii, and render, can be more complex and might involve using mock objects
    # or loading test images known to produce specific outputs.
        
    def test_resize_image(self):
        """Test resizing an image maintains the correct aspect ratio."""
        # Load a test image known to be 100x50 pixels
        self.studio.load('test_100x50.jpg')
        resized_image = self.studio._resize_image(new_width=50)
        expected_height = int(50 * 0.55)  # Adjusted for aspect ratio in _resize_image method
        self.assertEqual(resized_image.size, (50, expected_height))

    def test_convert_to_ascii(self):
        """Test converting a grayscale image to ASCII characters."""
        # Load a small grayscale image where you know the expected ASCII output
        self.studio.load('grayscale.jpg')
        ascii_art = self.studio._convert_to_ascii(self.studio.current_image)
        
        # Define what the expected ASCII output should be for the test image
        expected_output = (
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       ......::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@\n"
            "       .....:::::----====++++****####%%%%%@@@@@@@@"
        )
        self.assertEqual(ascii_art, expected_output)

    def test_render(self):
        """Test rendering an image to ASCII art produces the correct output."""
        # Load a test image with known characteristics
        self.studio.load('stadshuset.jpg')
        ascii_art = self.studio.render(new_width=50)
        # The expected output should be defined based on the known characteristics of test_image.jpg
        expected_output = (
            "==================================================\n"
            "==================================================\n"
            "======================-=++=-----------------------\n"
            "=======----------------=*#=-----------------------\n"
            "-----------------------=**=-----------------------\n"
            "----------------------+##@#+----------------------\n"
            "----------------------*##@@%----------------------\n"
            "----------------------*##@@%----------------------\n"
            "----------------------###@@%----------------------\n"
            "--------------------:-###@@%-:--------------------\n"
            "---------:--:::--:----###%@@-:::::-=-:------------\n"
            "-===-===+===++=++++++*###%@@%%%#*==#-::::---------\n"
            "*###****##*********###**#%@@@@@@@%%%#*==----------\n"
            "%%%%%##*#**************##%@@@@@@@@@%%%%%#===:.:--=\n"
            "%%%@%%#*#****************%%%@@@@@@@#%%%%####===**+\n"
            "%%%##%#**#############%#%%%%%%%%%%%%%##***+**++###\n"
            "**********************##%%%%#*******++++++=+=====+\n"
            "+++++++++++++++++++++**##%%%#***++++++++++++++++++\n"
        )
        self.assertEqual(ascii_art, expected_output)

if __name__ == '__main__':
    unittest.main()
