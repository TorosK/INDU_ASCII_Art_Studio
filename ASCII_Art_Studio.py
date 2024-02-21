# ASCII_Art_Studio.py

# Import the Image class from the Python Imaging Library (PIL) package.
# PIL, now known as Pillow, is a library that adds support for opening, manipulating,
# and saving many different image file formats. The Image class is central to this library,
# providing a unified interface for working with images across different formats.
# It is used in this script to load, convert to grayscale, resize, and access pixel data
# for the purpose of creating ASCII art representations of images.
from PIL import Image

# Define a string of ASCII characters ordered by perceived brightness, used to map pixel brightness to characters.
# ASCII characters are used to create a gradient of characters from light to dark
# which correspond to increasing levels of gray in an image.
ASCII_CHARS = "@%#*+=-:. "

# The width for the ASCII art output. This determines how many characters wide the ASCII art will be.
ASCII_ART_WIDTH_IN_CHARACTERS = 50
# Adjusts the height to ensure that the aspect ratio is maintained in a text display.
# For resizing the image to a specified width while maintaining the aspect ratio.

# This factor adjusts for the fact that text characters are usually taller than they are wide, which can distort the image.
# Adjusting for this helps maintain the original aspect ratio of the image in the ASCII art output.
FONT_ADJUSTMENT_FACTOR_FOR_DISPLAY_ASPECT_RATIO = 0.55

# Maximum grayscale value for a pixel, used in mapping pixel brightness to ASCII characters.
GRAYSCALE_MAX_VALUE = 256

class ASCII_Art_Studio:
    """
    A class to handle the conversion of images into ASCII art. It supports loading images,
    converting them to grayscale, resizing for appropriate aspect ratio in a text display,
    and rendering them as ASCII characters.
    """
    
    def __init__(self):
        """
        Initialize the ASCII Art Studio without any image pre-loaded. This sets up
        the internal state for future operations such as loading and rendering.
        """
        # Initializes the object without an image. `current_image` will hold the image being processed,
        # while `filename` stores the name of the file for reference.
        self.current_image = None  # Stores the current image as a PIL Image object
        self.filename = ''         # Stores the filename of the current image
    
    def load(self, filename):
        """
        Load an image from the given filename and convert it to grayscale. This method
        sets the loaded image as the current image to work with in the studio.
        
        Parameters:
        - filename: str, the path to the image file to be loaded.
        
        Returns:
        - str, a success message or an error message if the file cannot be loaded.
        """
        # Loads and converts an image to grayscale. This is the first step in preparing the image
        # for conversion to ASCII art. Grayscale simplifies the image to a single brightness value per pixel.
        try:
            with Image.open(filename) as img:
                # Convert the image to grayscale, which is needed for ASCII conversion
                self.current_image = img.convert('L')
                self.filename = filename
                return "Image loaded successfully."
        except FileNotFoundError:
            return "The specified file was not found."
        except IOError:
            # IOError is raised for problems like file not accessible, file is a directory,
            # or file has an incorrect format (not an image).
            return f"An IOError occurred: {e.strerror}. The file may not be accessible or may have an incorrect format."
        except Exception as e:
            # Catch-all for any other exceptions that may occur
            return f"An unexpected error occurred: {e}. Please check the file format and your access permissions."
    
    def info(self):
        """
        Retrieve information about the current image, including its filename and dimensions.
        
        Returns:
        - str, information about the current image or an indicator that no image is loaded.
        """
        if self.current_image:
            # Return formatted information about the image
            return f"Filename: {self.filename}\nSize: {self.current_image.size}"
        return "No image loaded"
    
    def _get_ascii_char(self, gray_value):
        # Maps a grayscale value to an ASCII character from the defined `ASCII_CHARS` string.
        # The mapping is based on the relative brightness of the grayscale value.
        index = int(gray_value / GRAYSCALE_MAX_VALUE * (len(ASCII_CHARS) - 1))
        return ASCII_CHARS[index]

    def _resize_image(self, new_width=ASCII_ART_WIDTH_IN_CHARACTERS):
        """
        Resizes the image to a specified width while maintaining the original aspect ratio.
        This is important for ensuring the ASCII art representation looks correct and not stretched.

        The new height is calculated based on the original aspect ratio (original height divided by original width)
        and adjusted by a factor to account for the typical character display aspect ratio, as characters
        are often taller than they are wide.

        Parameters:
        - new_width: int, the desired width for the ASCII art representation.

        Returns:
        - Image: a PIL Image object that has been resized to the new dimensions.
        """
        original_width, original_height = self.current_image.size
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio * FONT_ADJUSTMENT_FACTOR_FOR_DISPLAY_ASPECT_RATIO)
        return self.current_image.resize((new_width, new_height))
    
    def _convert_to_ascii(self, image):
        # Converts the resized grayscale image to ASCII art, line by line, by mapping each pixel's
        # brightness to an ASCII character.
        ascii_art = []
        for y in range(image.height):
            line = [self._get_ascii_char(image.getpixel((x, y))) for x in range(image.width)]
            ascii_art.append("".join(line) + '\n')  # Ensure each line is terminated with a newline character '\n'
        return ''.join(ascii_art)
    
    def render(self, new_width=ASCII_ART_WIDTH_IN_CHARACTERS):
        """
        Render the current image as ASCII art by first resizing it and then converting
        it to ASCII characters.
        
        Parameters:
        - new_width: int, an optional width for the ASCII art representation.
        
        Returns:
        - str, the ASCII art of the current image or an error message if no image is loaded.
        """
        if self.current_image is None:
            return "No image loaded to render."
        
        # Resize the image for text representation and convert it to ASCII art.
        ascii_image = self._resize_image(new_width)
        # Convert the resized image to ASCII art and return it
        return self._convert_to_ascii(ascii_image)