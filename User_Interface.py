# INDU_ASCII_Art_Studio\User_Interface.py

from ASCII_Art_Studio import ASCII_Art_Studio

class User_Interface:
    """
    A class dedicated to handling user interactions with the ASCII Art Studio application.
    It provides a command-line interface for users to execute various commands like loading images,
    rendering them as ASCII art, displaying image information, and quitting the application.
    """

    def __init__(self, art_studio):
        """
        Initialize the User_Interface with a reference to an ASCII_Art_Studio instance.
        
        Parameters:
        - art_studio: An instance of the ASCII_Art_Studio class to interact with.
        """
        self.art_studio = art_studio  # Reference to the art studio for command execution
        # Mapping of command strings to their respective methods for easy lookup and execution
        self.commands = {
            'load': self.load_command,
            'render': self.render_command,
            'info': self.info_command,
            'help': self.help_command,
            'quit': self.quit_command
        }
    
    def load_command(self, args):
        """
        Executes the 'load' command which loads an image file into the ASCII Art Studio.
        
        Parameters:
        - args: A list of command arguments where the first element is expected to be the filename.
        """
        if args:
            filename = args[0]  # Extract the filename from command arguments
            print(self.art_studio.load(filename))
        else:
            # Inform the user about the correct usage if no filename is provided
            print("No filename provided. Please use the command as: load <filename>")
    
    def render_command(self, args):
        """
        Executes the 'render' command to convert the currently loaded image into ASCII art.
        
        Parameters:
        - args: A list of command arguments where the first (optional) element can be the desired width.
        """
        # Check if a custom width is provided, otherwise use the default width of 50 characters
        new_width = int(args[0]) if args else 50
        print(self.art_studio.render(new_width=new_width))

    def info_command(self, args):
        """
        Executes the 'info' command to display information about the currently loaded image.
        
        Parameters:
        - args: A list of command arguments, not used in this method.
        """
        print(self.art_studio.info())

    def help_command(self, args):
        """
        Executes the 'help' command to display a list of available commands to the user.
        
        Parameters:
        - args: A list of command arguments, not used in this method.
        """
        self.display_help()

    def quit_command(self, args):
        """
        Executes the 'quit' command to exit the ASCII Art Studio application.
        
        Parameters:
        - args: A list of command arguments, not used in this method.
        """
        print("Bye!")
        exit(0)  # Terminate the program

    def display_help(self):
        """Displays a list of available commands and their descriptions to the user."""
        print("List of available commands:")
        print("  load <filename> - Load an image file as the current image.")
        print("  render [<width>] - Render the current image as ASCII art with optional width.")
        print("  info - Display information about the current image.")
        print("  quit - Exit the ASCII Art Studio.")
        print("  help - Show this list of available commands.")

    def run(self):
        """
        Starts the command loop for the user interface, continuously accepting commands
        until the 'quit' command is issued.
        """
        print("Welcome to ASCII Art Studio!\n")
        self.display_help()
        
        while True:
            try:
                # Split the user input into command and arguments for processing
                command_input = input("AAS: ").strip().split()
                command = command_input[0].lower()  # Command is case-insensitive
                args = command_input[1:]  # Any elements after the command are arguments
                
                # Execute the corresponding command method if the command is recognized
                if command in self.commands:
                    self.commands[command](args)
                else:
                    print("Unknown command. Type 'help' for a list of available commands.")
            except KeyError:
                # Handle cases where the command format is incorrect
                print("Invalid command format. Type 'help' for a list of available commands.")
            except ValueError as ve:
                # Handle value errors, such as invalid integers for width
                print(f"Value Error: {ve}")
            except IOError as io:
                # Handle IO errors, which may occur when accessing files
                print(f"IO Error: {io}")
            except Exception as e:
                # Catch-all for any other unexpected errors
                print(f"An unexpected error occurred: {e}")
            
if __name__ == "__main__":
    studio = ASCII_Art_Studio()
    ui = User_Interface(studio)
    ui.run()