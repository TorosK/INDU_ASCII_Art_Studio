ASCII Art Studio
ASCII Art Studio is a Python application that allows users to convert images into ASCII art. ASCII art is a graphic design technique that uses printable characters from the ASCII standard to create images. This project provides a simple command-line interface for users to load images, convert them to ASCII art, and view information about the images.

Features
Load Images: Users can load JPG, PNG, and other common image formats.
Render ASCII Art: Converts the loaded images into ASCII art, maintaining the original aspect ratio.
Image Information: Displays the filename and size of the currently loaded image.
Help: Provides a list of available commands.
Getting Started
To use ASCII Art Studio, clone the repository and run the User_Interface.py script. Ensure you have Python and the required packages installed.

python User_Interface.py

Follow the on-screen prompts to load images and convert them to ASCII art.

Why from PIL import Image?
The line from PIL import Image imports the Image class from the Python Imaging Library (PIL), which is now known as Pillow. Pillow is a fork of PIL and provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

Reasons for using Pillow:
Image Loading and Processing: Pillow allows us to easily load images from files, convert them between different formats, and process them in various ways. In ASCII Art Studio, we use Pillow to load images and convert them to grayscale, which is a crucial step in generating ASCII art.
Compatibility: Pillow supports a wide range of image formats, making it versatile for different types of images users might want to convert to ASCII art.
Ease of Use: The Pillow library provides a straightforward and intuitive interface for working with images, which is ideal for a project like ASCII Art Studio that aims to be user-friendly.
By using Pillow, ASCII Art Studio can efficiently handle the image processing tasks required to transform images into ASCII art, making it a key component of the project.

# TESTING:

python -m unittest Test_ASCII_Art_Studio.py