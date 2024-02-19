# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\ASCII_Art_Studio.py

from PIL import Image

# ASCII characters are used to create a gradient of characters from light to dark
# which correspond to increasing levels of gray in an image.
ASCII_CHARS = "@%#*+=-:. "

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
            return "The specified file has an incorrect format or is not accessible."
    
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
        """
        Determine which ASCII character to use based on the grayscale value.
        
        Parameters:
        - gray_value: int, a value from 0 to 255 representing the grayscale level.
        
        Returns:
        - str, a single ASCII character.
        """
        # Map the grayscale value to one of the ASCII characters based on its intensity
        return ASCII_CHARS[gray_value * len(ASCII_CHARS) // 256]
    
    def _resize_image(self, new_width=50):
        """
        Resize the image to a specified width while maintaining the aspect ratio.
        Adjusts the height to ensure that the aspect ratio is maintained in a text display.
        
        Parameters:
        - new_width: int, the desired width of the ASCII art.
        
        Returns:
        - Image, a new PIL Image object with the adjusted dimensions.
        """
        (original_width, original_height) = self.current_image.size
        aspect_ratio = original_height / float(original_width)
        # Fonts typically have characters that are taller than they are wide, hence the
        # adjustment factor of 0.55 to compensate for the display aspect ratio.
        new_height = int(aspect_ratio * new_width * 0.55)
        # Resize and return the new image
        return self.current_image.resize((new_width, new_height))
    
    def _convert_to_ascii(self, image):
        """
        Convert the image to ASCII art by mapping each pixel's grayscale value to an ASCII character.
        
        Parameters:
        - image: Image, the PIL Image object to be converted.
        
        Returns:
        - str, the ASCII art representation of the image as a string.
        """
        ascii_art = []
        for y in range(image.height):
            # Generate a line of ASCII characters for each row of pixels
            line = [self._get_ascii_char(image.getpixel((x, y)))
                    for x in range(image.width)]
            ascii_art.append("".join(line))
        # Join all lines into a single string separated by newlines
        return "\n".join(ascii_art)
    
    def render(self, new_width=50):
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