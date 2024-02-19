from PIL import Image

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
        
        Returns:
        - A string indicating success or error message.
        """
        try:
            with Image.open(filename) as img:
                self.current_image = img.convert('L')  # Convert to grayscale
                self.filename = filename
                return "Image loaded successfully."
        except FileNotFoundError:
            return "The specified file was not found."
        except ValueError:
            return "The specified file has an incorrect format."
    
    def info(self):
        """
        Print information about the current image.
        
        Returns:
        - A string with information or a message indicating no image is loaded.
        """
        if self.current_image:
            return f"Filename: {self.filename}\nSize: {self.current_image.size}"
        else:
            return "No image loaded"
    
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
        (The new_width parameter of the _adjust_dimensions method is set to a default value of 50. This means when this method is called without specifying the new_width parameter, it uses 50 as the width for the ASCII art.)
        
        Returns:
        - A new image with adjusted dimensions.
        """
        (original_width, original_height) = image.size
        aspect_ratio = original_height / float(original_width)
        # Adjust for the fact that characters are generally taller than they are wide
        new_height = int(aspect_ratio * new_width * 0.55)
        new_dim = (new_width, new_height)
        
        return image.resize(new_dim)
    
    def render(self):
        """
        Render the current image as ASCII art.
        
        Returns:
        - A string representing the ASCII art of the current image or an error message.
        """
        if self.current_image is None:
            return "No image loaded to render."
        
        try:
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
        except Exception as e:
            return f"An error occurred while rendering: {e}"

def main():
    studio = ASCII_Art_Studio()
    print("Welcome to ASCII Art Studio!\n")
    print("List of available commands:")
    print("  load <filename> - Load an image file as the current image.")
    print("  render          - Render the current image as ASCII art.")
    print("  info            - Display information about the current image.")
    print("  quit            - Exit the ASCII Art Studio.")
    print("  help            - Show the list of available commands.\n")

    while True:
        try:
            command = input("AAS: ").strip().lower()
            if command.startswith('load '):
                filename = command[5:]
                print(studio.load(filename))
            elif command == 'render':
                print(studio.render())
            elif command == 'info':
                print(studio.info())
            elif command == 'help':
                print("List of available commands:")
                print("  load <filename> - Load an image file as the current image.")
                print("  render          - Render the current image as ASCII art.")
                print("  info            - Display information about the current image.")
                print("  quit            - Exit the ASCII Art Studio.")
                print("  help            - Show the list of available commands.\n")
            elif command == 'quit':
                print("Bye!")
                break
            else:
                print("Unknown command. Type 'help' for a list of available commands.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
