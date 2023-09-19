import os
import shutil
from PIL import Image
from datetime import datetime

# Define the directory where your images are located
image_folder = "images"

# Get a list of image files in the folder
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Sort the image files by creation date (oldest to newest)
image_files.sort(key=lambda x: os.path.getctime(os.path.join(image_folder, x)))

# Rename the images sequentially from 1 to n
for i, old_name in enumerate(image_files, start=1):
    # Determine the file extension
    file_extension = os.path.splitext(old_name)[1].lower()

    # Create a new name with a leading zero for single-digit numbers
    new_name = f"{i:02d}{file_extension}"

    # Get the full paths of the old and new files
    old_path = os.path.join(image_folder, old_name)
    new_path = os.path.join(image_folder, new_name)

    # Rename the file
    os.rename(old_path, new_path)

    print(f"Renamed '{old_name}' to '{new_name}'")

print("Renaming completed successfully.")
