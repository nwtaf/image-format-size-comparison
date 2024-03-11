import os
import glob
from pathlib import Path
from ultralytics import YOLO
import time
import matplotlib.pyplot as plt

# Load model
model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model

# Get all image file paths from a directory
current_dir = Path(__file__).parent
image_dir = current_dir / '..' / 'data' / 'resized_images'
source = str(os.path.join(image_dir, '*')) # may or may not need the glob() or str() function

# Create folder for detected images
output_folder = current_dir / '..' / 'data' / 'detected_images'
output_folder.mkdir(parents=True, exist_ok=True)

# Run inference on the source
results = model(source, stream=True, save=True)  # generator of Results objects

# Process results for this image
for result in results:
    # Save detected image with an identifier
    # filename = os.path.basename(source)
    # output_path = output_folder / (filename + '_detected.jpg')
    # result.save(filename=str(output_path))  # Save the annotated image with detections
    probs = result.probs  # Probs object for classification outputs
    speeds = result.speed  # Speed object for inference times

# Save the detection probabilities and inference speeds
'''probs_file = current_dir / '..' / 'data' / 'probs.txt'
speeds_file = current_dir / '..' / 'data' / 'speeds.txt'
with open(probs_file, 'w') as f:
    f.write('\n'.join(map(str, probs)))
with open(speeds_file, 'w') as f:
    f.write('\n'.join(map(str, speeds)))
'''

# Generate graphs
# Create folder for graphs
graphs_folder = current_dir / '..' / 'data' / 'graphs'
graphs_folder.mkdir(parents=True, exist_ok=True)

# Create a graph for the inference speeds
plt.figure()
plt.plot(list(speeds.values()))  # Plot the values of the dictionary
plt.title('Inference Speeds')
plt.xlabel('Inference')
plt.ylabel('Speed')
plt.show()
# plt.savefig(str(graphs_folder / 'inference_speeds.png'))

# Create a graph for the detection probabilities
'''plt.figure()
plt.plot(list(probs.values()))
plt.title('Detection Probabilities')
plt.xlabel('Detection')
plt.ylabel('Probability')
# plt.savefig(str(graphs_folder / 'detection_probabilities.png'))
'''