import os
import random
import shutil
from pathlib import Path

def create_subset(source_dir, dest_dir, num_images):
    """Copies a random subset of images and their labels."""
    source_images = Path(source_dir) / "images"
    source_labels = Path(source_dir) / "labels"

    dest_images = Path(dest_dir) / "images"
    dest_labels = Path(dest_dir) / "labels"

    # Create destination directories
    dest_images.mkdir(parents=True, exist_ok=True)
    dest_labels.mkdir(parents=True, exist_ok=True)

    # Get a list of all image files (works with .jpg, .png, etc.)
    image_files = list(source_images.glob("*.*"))
    
    # Get a random sample
    if len(image_files) > num_images:
        sampled_images = random.sample(image_files, num_images)
    else:
        print(f"Warning: Requested {num_images} but only {len(image_files)} available. Using all.")
        sampled_images = image_files

    # Copy images and their corresponding labels
    for img_path in sampled_images:
        label_path = source_labels / f"{img_path.stem}.txt"
        
        shutil.copy(img_path, dest_images)
        if label_path.exists():
            shutil.copy(label_path, dest_labels)
    
    print(f"Copied {len(sampled_images)} images and labels to {dest_dir}")

# --- Configuration ---
FULL_DATASET_PATH = Path("./data/lp")
SUBSET_PATH = Path("./data/lp_small")

# --- Run the script ---
print("Creating training subset...")
create_subset(FULL_DATASET_PATH / "train", SUBSET_PATH / "train", 500)

print("\nCreating validation subset...")
create_subset(FULL_DATASET_PATH / "valid", SUBSET_PATH / "valid", 50)