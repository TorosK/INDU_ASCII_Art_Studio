# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\ASCII_Art_Studio.py

from PIL import Image
import numpy as np
import unittest

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

class ASCII_Art_Studio:
    def __init__(self):
        """Initialize the ASCII_Art_Studio with no image loaded."""
        self.current_image = None
        self.filename = ''
    
    def load(self, filename):
        """
        Load an image file as the current image.
        
        Parameters:
        - filename: The path to the image file.
        
        Raises:
        - FileNotFoundError: If the file does not exist.
        - ValueError: If the file format is incorrect.
        """
        try:
            with Image.open(filename) as img:
                self.current_image = img.convert('L')  # Convert to grayscale
                self.filename = filename
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found.")
        except ValueError:
            raise ValueError("The specified file has an incorrect format.")
    
    def info(self):
        """
        Print information about the current image.
        
        Output:
        - Prints the filename and size if an image is loaded.
        - Prints "No image loaded" if no image is currently loaded.
        """
        if self.current_image:
            print(f"Filename: {self.filename}")
            print(f"Size: {self.current_image.size}")
        else:
            print("No image loaded")
    
    def _get_ascii_char(self, gray_value):
        """
        Map a grayscale value to an ASCII character.
        
        Parameters:
        - gray_value: A value from 0 to 255 representing the brightness of a pixel.
        
        Returns:
        - A single ASCII character as a string.
        """
        return ASCII_CHARS[gray_value * len(ASCII_CHARS) // 256]
    
    def _adjust_dimensions(self, image, new_width=50):
        """
        Adjust the dimensions of the image to maintain the aspect ratio.
        
        Parameters:
        - image: The image to adjust.
        - new_width: The desired width of the ASCII art.
        
        Returns:
        - A new image with adjusted dimensions.
        """
        (original_width, original_height) = image.size
        aspect_ratio = original_height/float(original_width)
        # Adjust for the fact that characters are generally taller than they are wide
        new_height = int(aspect_ratio * new_width * 0.55)
        new_dim = (new_width, new_height)
        
        return image.resize(new_dim)
    
    def render(self):
        """
        Render the current image as ASCII art.
        
        Returns:
        - A string representing the ASCII art of the current image.
        """
        if self.current_image is None:
            raise ValueError("No image loaded.")
        
        # Resize the image to maintain aspect ratio
        ascii_image = self._adjust_dimensions(self.current_image)
        
        # Convert the image to ASCII characters
        ascii_art = []
        for y in range(ascii_image.height):
            line = [self._get_ascii_char(ascii_image.getpixel((x, y)))
                    for x in range(ascii_image.width)]
            ascii_art.append("".join(line))
        
        # Return the ASCII art as a string
        return "\n".join(ascii_art)

# Example usage of the ASCIIArtStudio class
def main():
    studio = ASCII_Art_Studio()
    studio.load('path_to_image.jpg')  # Replace with actual image path
    studio.info()
    print(studio.render())

if __name__ == "__main__":
    main()

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
    
    # ... (additional unit tests)

if __name__ == "__main__":
    unittest.main()
