# Image Format Size Comparison
This project provides a Python script to visualize the impact of image resizing on file size across various image formats including JPEG, PNG, and BMP. The script generates individual graphs for each format and a comparison graph for all formats. The graphs are saved as PNG files in the `data/graphs` directory.

## Installation
Before running the script, make sure required Python packages installed. Install them with pip:

`pip install opencv-python matplotlib`

## Usage
The script takes the path of an image file ('data/RPi.png' by default) and an output folder (`data/graphs`) as arguments. It resizes the image to various percentages of the original size, saves the resized images in the specified formats, and generates graphs of the file sizes. Simply running `main.py` will resize the image to percentages ranging from 10% to 100% of the original size, save the resized images in JPEG, PNG, and BMP formats in the output folder, and generate the graphs in a "graphs" subfolder within the output folder.

You can customize the formats and resize percentages by modifying the formats and resize_percents parameters in the resize_and_save_image function.

Default input image:
<img src="/data/RPi.png" width="200">

Example output comparison graph:
<img src="/data/graphs/comparison_graph.png>