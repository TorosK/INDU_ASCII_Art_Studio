# C:\Users\TorosKutlu\Desktop\SU Programming Techniques\INDU_ASCII_Art_Studio\User_Interface.py

from ASCII_Art_Studio import ASCII_Art_Studio

class User_Interface:
    """Class to handle user interactions for the ASCII Art Studio."""

    def __init__(self, art_studio):
        self.art_studio = art_studio
        self.commands = {
            'load': self.load_command,
            'render': self.render_command,
            'info': self.info_command,
            'help': self.help_command,
            'quit': self.quit_command
        }
    
    def load_command(self, args):
        """Handle the 'load' command."""
        if args:
            filename = args[0]
            print(self.art_studio.load(filename))
        else:
            print("No filename provided. Please use the command as: load <filename>")
    
    def render_command(self, args):
        """Handle the 'render' command."""
        # Optional: Allow user to specify width
        new_width = int(args[0]) if args else 50
        print(self.art_studio.render(new_width=new_width))

    def info_command(self, args):
        """Handle the 'info' command."""
        print(self.art_studio.info())

    def help_command(self, args):
        """Handle the 'help' command."""
        self.display_help()

    def quit_command(self, args):
        """Handle the 'quit' command."""
        print("Bye!")
        exit(0)

    def display_help(self):
        """Display available commands to the user."""
        print("List of available commands:")
        print("  load <filename> - Load an image file as the current image.")
        print("  render [<width>] - Render the current image as ASCII art with optional width.")
        print("  info - Display information about the current image.")
        print("  quit - Exit the ASCII Art Studio.")
        print("  help - Show this list of available commands.")

    def run(self):
        """Run the user interface command loop."""
        print("Welcome to ASCII Art Studio!\n")
        self.display_help()
        
        while True:
            try:
                command_input = input("AAS: ").strip().split()
                command = command_input[0].lower()
                args = command_input[1:]
                
                if command in self.commands:
                    self.commands[command](args)
                else:
                    print("Unknown command. Type 'help' for a list of available commands.")
            except KeyError:
                print("Invalid command format. Type 'help' for a list of available commands.")
            except ValueError as ve:
                print(f"Value Error: {ve}")
            except IOError as io:
                print(f"IO Error: {io}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            
if __name__ == "__main__":
    studio = ASCII_Art_Studio()
    ui = User_Interface(studio)
    ui.run()
