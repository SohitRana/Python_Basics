import os
import random
import shutil

# Configuration
dataset_dir = 'dataset/images'  # directory with all images
labels_dir = 'dataset/labels'   # directory with all label files (same name as images but .txt)
output_dir = 'dataset/split'    # destination folder
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Create destination directories
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_dir, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, split, 'labels'), exist_ok=True)

# Collect all images
images = [f for f in os.listdir(dataset_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(images)

# Split dataset
total = len(images)
train_end = int(total * train_ratio)
val_end = train_end + int(total * val_ratio)

train_images = images[:train_end]
val_images = images[train_end:val_end]
test_images = images[val_end:]

def copy_files(image_list, split):
    for image_name in image_list:
        label_name = os.path.splitext(image_name)[0] + '.txt'

        src_img = os.path.join(dataset_dir, image_name)
        src_lbl = os.path.join(labels_dir, label_name)

        dst_img = os.path.join(output_dir, split, 'images', image_name)
        dst_lbl = os.path.join(output_dir, split, 'labels', label_name)

        shutil.copyfile(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.copyfile(src_lbl, dst_lbl)

# Copy files to destination
copy_files(train_images, 'train')
copy_files(val_images, 'val')
copy_files(test_images, 'test')

print(f"Split complete:\n - Train: {len(train_images)}\n - Val: {len(val_images)}\n - Test: {len(test_images)}")

