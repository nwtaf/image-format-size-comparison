# image-format-size-comparison
Visualize the impact of image resizing on file size across various image formats including JPEG, PNG, GIF, and different bitmap color depths. Includes command line options.

## Installation
Before running the script, make sure the matplotlib package is installed:

`pip install matplotlib`

## Usage
To generate a graph for a specific image format, run the script with desired format as an argument. The available formats are `jpeg`, `png`, `gif`, `bmp_mono`, `bmp_16`, `bmp_256`, and `bmp_24bit`. For example, to plot the graph for JPEG files:

`python ifsc.py jpeg`

To generate graphs for all supported image types at once:

`python ifsc.py all`
