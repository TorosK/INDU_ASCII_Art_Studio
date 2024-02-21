# User_Interface.py

from ASCII_Art_Studio import ASCII_Art_Studio

class User_Interface:
    """
    A class dedicated to handling user interactions with the ASCII Art Studio application.
    Provides a command-line interface for users to execute commands such as loading images,
    rendering ASCII art, displaying image info, and quitting the application.
    """

    def __init__(self, art_studio):
        """
        Initialize the User_Interface with a reference to an ASCII_Art_Studio instance.

        Parameters:
        - art_studio: An instance of ASCII_Art_Studio class for performing image to ASCII art conversions.
        """
        self.art_studio = art_studio  # Reference to the ASCII Art Studio for processing images
        self.running = True  # Flag to control the main command loop

        # Commands dictionary maps command text to their handling methods for efficient command processing
        self.commands = {
            'load': self.load_command,
            'render': self.render_command,
            'info': self.info_command,
            'help': self.help_command,
            'quit': self.quit_command
        }
    
    def load_command(self, args):
        """
        Handles the 'load' command to load an image file into the ASCII Art Studio.

        Parameters:
        - args: List of command arguments, expects the first element to be the filename.
        """
        if args:
            filename = args[0]  # First argument is assumed to be the filename
            print(self.art_studio.load(filename))  # Load the image and print the result
        else:
            # Make sure this message matches exactly with the expected message in the test case
            print("No filename provided. Please use the command as: load <filename>")

    def render_command(self, args):
        """
        Handles the 'render' command to convert the currently loaded image into ASCII art.

        Parameters:
        - args: List of command arguments, the first (optional) element can specify a custom width.
        """
        new_width = int(args[0]) if args else 50  # Default width is 50 characters if not specified
        print(self.art_studio.render(new_width=new_width))  # Render and print the ASCII art

    def info_command(self, args):
        """
        Handles the 'info' command to display information about the currently loaded image.

        Parameters:
        - args: List of command arguments, not used in this method.
        """
        print(self.art_studio.info())  # Print information about the current image

    def help_command(self, args):
        """
        Handles the 'help' command to display a list of available commands.

        Parameters:
        - args: List of command arguments, not used in this method.
        """
        self.display_help()  # Display the help text with available commands

    def quit_command(self, args):
        """
        Handles the 'quit' command to exit the ASCII Art Studio application.

        Parameters:
        - args: List of command arguments, not used in this method.
        """
        print("Exiting ASCII Art Studio. Goodbye!")        
        self.running = False  # Update the running flag to stop the command loop

    def display_help(self):
        """Displays a list of available commands and their usage to the user."""
        help_text = """
        Available commands:
          load <filename>   : Load an image file into the studio.
          render [<width>]  : Render the loaded image as ASCII art with an optional width.
          info              : Display information about the current image.
          help              : Show this help message.
          quit              : Exit the ASCII Art Studio.
        """
        print(help_text.strip())

    def run(self):
        """
        Starts the command loop for the user interface, accepting and processing commands until 'quit'.
        """
        print("Welcome to ASCII Art Studio!\nType 'help' for a list of commands.")
        while self.running:
            try:
                command_input = input("AAS> ").strip().split()
                command = command_input[0].lower()  # Convert command to lowercase for case-insensitive comparison
                args = command_input[1:]  # Separate the command from its arguments

                if command in self.commands:
                    self.commands[command](args)  # Execute the command if recognized
                else:
                    print("Unknown command. Type 'help' for a list of commands.")
            except KeyError:
                print("Invalid command format. Type 'help' for command usage.")
            except ValueError as ve:
                print(f"Value Error: {ve}. Check command arguments.")
            except IOError as io:
                print(f"IO Error: {io}. Check file paths and permissions.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again or check the command syntax.")

if __name__ == "__main__":
    studio = ASCII_Art_Studio()  # Create an instance of ASCII_Art_Studio
    ui = User_Interface(studio)  # Initialize the User_Interface with the studio instance
    ui.run()  # Start the command loop