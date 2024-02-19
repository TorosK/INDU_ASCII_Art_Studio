# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\ASCII_Art_Studio.py

from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

class ASCII_Art_Studio:
    """Class to convert images to ASCII art."""
    
    def __init__(self):
        """Initialize the ASCII_Art_Studio with no image loaded."""
        self.current_image = None
        self.filename = ''
    
    def load(self, filename):
        """Load an image file as the current image."""
        try:
            with Image.open(filename) as img:
                self.current_image = img.convert('L')  # Convert to grayscale
                self.filename = filename
                return "Image loaded successfully."
        except FileNotFoundError:
            return "The specified file was not found."
        except IOError:
            return "The specified file has an incorrect format or is not accessible."
    
    def info(self):
        """Print information about the current image."""
        if self.current_image:
            return f"Filename: {self.filename}\nSize: {self.current_image.size}"
        return "No image loaded"
    
    def _get_ascii_char(self, gray_value):
        """Map a grayscale value to an ASCII character."""
        return ASCII_CHARS[gray_value * len(ASCII_CHARS) // 256]
    
    def _resize_image(self, new_width=50):
        """Resize the image to maintain the aspect ratio."""
        (original_width, original_height) = self.current_image.size
        aspect_ratio = original_height / float(original_width)
        new_height = int(aspect_ratio * new_width * 0.55)
        return self.current_image.resize((new_width, new_height))
    
    def _convert_to_ascii(self, image):
        """Convert the image to an ASCII art representation."""
        ascii_art = []
        for y in range(image.height):
            line = [self._get_ascii_char(image.getpixel((x, y)))
                    for x in range(image.width)]
            ascii_art.append("".join(line))
        return "\n".join(ascii_art)
    
    def render(self, new_width=50):
        """Render the current image as ASCII art."""
        if self.current_image is None:
            return "No image loaded to render."
        
        ascii_image = self._resize_image(new_width)
        return self._convert_to_ascii(ascii_image)