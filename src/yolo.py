import os
import glob
from pathlib import Path
import PIL
from ultralytics import YOLO

import matplotlib.pyplot as plt

# Load model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

current_dir = Path(__file__).parent
resized_images_dir = current_dir / '..' / 'data' / 'resized_images'
png_images_dir = resized_images_dir / 'png'
detected_images_dir = current_dir / '..' / 'data' / 'detected_images'
graphs_dir = current_dir / '..' / 'data' / 'graphs'

# Lists to store times and image sizes
preprocess_times = []
inference_times = []
postprocess_times = []
total_times = []
image_sizes = []

# Get list of image paths
image_paths = list(png_images_dir.glob('*'))

# Process each image individually
for image_path in image_paths:
    image_size_bytes = os.path.getsize(image_path)
    image_size_wh = PIL.Image.open(image_path).size
    # Run inference on a single image
    results = model(source=image_path, save=False, classes=[15], imgsz=image_size_wh, project=str(detected_images_dir / 'png'))  # return a list of Results objects

    speeds = results[0].speed # Speed object for inference times

    # Calculate times and image size
    preprocess_times.append(speeds['preprocess'])
    inference_times.append(speeds['inference'])
    postprocess_times.append(speeds['postprocess'])
    total_times.append(sum(speeds.values()))
    image_sizes.append(image_size_bytes)
    
print(f'total times: {total_times}')
print(f'image sizes: {image_sizes}')
'''
# Generate graph
plt.figure()
plt.plot(image_sizes, preprocess_times, label='Preprocess Time')
plt.plot(image_sizes, inference_times, label='Inference Time')
plt.plot(image_sizes, postprocess_times, label='Postprocess Time')
plt.plot(image_sizes, total_times, label='Total Time')
plt.title('PNG: Time vs Image Size')
plt.xlabel('Image Size (bytes)')
plt.ylabel('Time (milliseconds)')
plt.legend()
plt.show()
# plt.savefig(str(graphs_dir / 'png_time_vs_image_size.png'))
'''