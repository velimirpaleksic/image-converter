import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import messagebox


def convert_image(input_path, output_path, output_format):
    """
    Converts a single image to the desired format.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the converted image.
        output_format (str): Desired image format (e.g., 'JPEG', 'PNG', 'WEBP', 'HEIC', 'ICO').
    """
    try:
        with Image.open(input_path) as img:
            if output_format.upper() == "ICO":
                img.save(output_path, format=output_format.upper(), sizes=[(256, 256)])
            else:
                img = img.convert("RGB")
                img.save(output_path, output_format.upper())
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", f"Failed to convert {input_path}: {e}")
        sys.exit(1)


def get_unique_output_path(directory, base_name, extension):
    """
    Generates a unique file name if the file already exists.

    Args:
        directory (str): Directory where the file will be saved.
        base_name (str): Base name of the file.
        extension (str): File extension.

    Returns:
        str: Unique file path.
    """
    counter = 1
    output_path = os.path.join(directory, f"{base_name}.{extension}")
    while os.path.exists(output_path):
        output_path = os.path.join(directory, f"{base_name}_{counter}.{extension}")
        counter += 1
    return output_path


def batch_convert_images(input_dir, output_format):
    """
    Batch converts all images in a directory to the desired format.

    Args:
        input_dir (str): Directory containing the input images.
        output_format (str): Desired image format (e.g., 'JPEG', 'PNG', 'WEBP', 'HEIC', 'ICO').
    """
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            name, _ = os.path.splitext(filename)
            output_path = get_unique_output_path(input_dir, name, output_format.lower())
            convert_image(input_path, output_path, output_format)


def convert_single_image(input_path, output_format):
    """
    Converts a single image to the desired format.

    Args:
        input_path (str): Path to the input image.
        output_format (str): Desired image format.
    """
    directory = os.path.dirname(input_path)
    name, _ = os.path.splitext(os.path.basename(input_path))
    output_path = get_unique_output_path(directory, name, output_format.lower())
    convert_image(input_path, output_path, output_format)


def main():
    if len(sys.argv) < 3:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Usage Error", "Usage: python image_converter.py <input_path_or_dir> <output_format>")
        sys.exit(1)

    input_path_or_dir = sys.argv[1]
    output_format = sys.argv[2].lower()

    supported_formats = {"png", "jpeg", "jpg", "webp", "heic", "ico"}
    if output_format not in supported_formats:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Format Error", f"Unsupported format: {output_format}. Supported formats are {', '.join(supported_formats)}.")
        sys.exit(1)

    if os.path.isdir(input_path_or_dir):
        batch_convert_images(input_path_or_dir, output_format)
    elif os.path.isfile(input_path_or_dir):
        convert_single_image(input_path_or_dir, output_format)
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Path Error", "Error: The provided path does not exist.")
        sys.exit(1)

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Success", "Conversion completed!")


if __name__ == "__main__":
    main()