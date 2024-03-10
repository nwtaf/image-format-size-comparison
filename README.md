# Image Format Size Comparison
This project provides a Python script to visualize the impact of image resizing on file size across various image formats including JPEG, PNG, and BMP. The script generates individual graphs for each format and a comparison graph for all formats. The graphs are saved as PNG files in a specified folder.

## Installation
Before running the script, make sure you have the required Python packages installed. You can install them with pip:

`pip install opencv-python matplotlib`

## Usage
The script takes the path of an image file and an output folder as arguments. It resizes the image to various percentages of the original size, saves the resized images in the specified formats, and generates graphs of the file sizes.

Example of how to use the script:

`python resize_and_save_image.py /path/to/image /path/to/output/folder`

This will resize the image to percentages ranging from 10% to 100% of the original size, save the resized images in JPEG, PNG, and BMP formats in the output folder, and generate the graphs in a "graphs" subfolder within the output folder.

You can customize the formats and resize percentages by modifying the formats and resize_percents parameters in the resize_and_save_image function.