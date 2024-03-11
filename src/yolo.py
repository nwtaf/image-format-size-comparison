import os
import glob
from pathlib import Path
from ultralytics import YOLO

# Load model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# Get all image file paths from a directory
current_dir = Path(__file__).parent
image_dir = current_dir / '..' / 'data'
image_files = glob.glob(os.path.join(image_dir, '*'))

# Run batched inference on all images
results = model(image_files)  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    probs = result.probs  # Probs object for classification outputs
    result.save(filename='result.jpg')  # save to disk