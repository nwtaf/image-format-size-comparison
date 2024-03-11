import cv2
from pathlib import Path
import matplotlib.pyplot as plt

def resize_and_save_image(image_path, output_folder, formats=('jpeg', 'png', 'bmp'), resize_percents=range(10, 101, 10)):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    original_image = cv2.imread(str(image_path))
    original_size = original_image.shape[:2]  # Get the height and width

    image_sizes = {percent: {file_format: None for file_format in formats} for percent in resize_percents}

    for percent in resize_percents:
        for fmt in formats:
            new_size = tuple(reversed([int(size * percent / 100) for size in original_size]))  # Width, Height
            resized_image = cv2.resize(original_image, new_size)

            file_name = f"resized_{percent}percent.{fmt}"
            file_path = output_folder / file_name
            cv2.imwrite(str(file_path), resized_image)

            image_sizes[percent][fmt] = file_path.stat().st_size

    for percent, formats in image_sizes.items():
        for fmt, size in formats.items():
            print(f"Size for {percent}% resize as {fmt}: {size} bytes")
    
    return image_sizes

def generate_graphs(image_sizes, graphs_folder):
    graphs_folder = Path(graphs_folder)
    graphs_folder.mkdir(parents=True, exist_ok=True)

    all_sizes = {fmt: [] for fmt in image_sizes[next(iter(image_sizes))]}
    
    for fmt in all_sizes:
        plt.figure()
        sizes = [image_sizes[percent][fmt] for percent in image_sizes]
        plt.plot(list(image_sizes.keys()), sizes)
        plt.title(f'Size vs Resize Percentage ({fmt})')
        plt.xlabel('Resize Percentage')
        plt.ylabel('Size (bytes)')
        plt.savefig(str(graphs_folder / f'{fmt}_graph.png'))
        all_sizes[fmt] = sizes

    plt.figure()
    for fmt, sizes in all_sizes.items():
        plt.plot(list(image_sizes.keys()), sizes, label=fmt)
    plt.title('Size vs Resize Percentage (All Formats)')
    plt.xlabel('Resize Percentage')
    plt.ylabel('Size (bytes)')
    plt.legend()
    plt.savefig(str(graphs_folder / 'comparison_graph.png'))

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    image_path = current_dir / '..' / 'data' / 'gremlin.jpg'
    output_folder = current_dir / '..' / 'data' / 'resized_images'
    graphs_folder = current_dir / '..' / 'data' / 'graphs'

    image_path = image_path.resolve()
    output_folder = output_folder.resolve()
    graphs_folder = graphs_folder.resolve()

    image_sizes = resize_and_save_image(image_path, output_folder)
    generate_graphs(image_sizes, graphs_folder)