import cv2
from pathlib import Path

def resize_and_save_image(image_path, output_folder, formats=('jpeg', 'png', 'bmp'), resize_percents=range(10, 101, 10)):
    """
    Resizes an image to percentages of the original size and saves the resized images in the specified formats.
    
    :param image_path: Path to the original image.
    :param output_folder: Folder to save the resized images.
    :param formats: Tuple of image formats to save, defaults to ('jpeg', 'png').
    :param resize_percents: Range of percentages to resize, defaults to range(10, 101, 10).
    :return: None
    """
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    original_image = cv2.imread(str(image_path))
    original_size = original_image.shape[:2]  # Get the height and width

    # Dictionary to hold image sizes for all formats and resize percentages
    image_sizes = {percent: {file_format: None for file_format in formats} for percent in resize_percents}

    for percent in resize_percents:
        for fmt in formats:
            # Calculate new size and resize image
            new_size = tuple(reversed([int(size * percent / 100) for size in original_size]))  # Width, Height
            resized_image = cv2.resize(original_image, new_size)

            # Define file name and save image in the specified format
            file_name = f"resized_{percent}percent.{fmt}"
            file_path = output_folder / file_name
            cv2.imwrite(str(file_path), resized_image)

            # Record the file size
            image_sizes[percent][fmt] = file_path.stat().st_size

    # Print and/or return the sizes
    for percent, formats in image_sizes.items():
        for fmt, size in formats.items():
            print(f"Size for {percent}% resize as {fmt}: {size} bytes")
    
    return image_sizes

# Example usage
if __name__ == "__main__":
    # Define paths
    current_dir = Path(__file__).parent
    print(current_dir)
    image_path = current_dir / '..' / 'data' / 'RPi.png' # Path of sample image
    output_folder = current_dir / '..' / 'data' / 'resized_images' # Folder to save resized images

    # Resolve the paths to handle the '..' parts
    image_path = image_path.resolve()
    output_folder = output_folder.resolve()

    image_sizes = resize_and_save_image(image_path, output_folder)