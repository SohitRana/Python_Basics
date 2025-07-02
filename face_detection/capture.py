import cv2
import os

# Path to your video file (use raw string or double backslashes)
video_path = r"C:\\Users\\Akhil\\Videos\\5.mp4.mp4"

# Get the path to your Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Folder on Desktop to save images
output_folder = os.path.join(desktop_path, "cam_1")
os.makedirs(output_folder, exist_ok=True)

# Open the video
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print(f"Error: Cannot open video file {video_path}")
    exit()

frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every frame as an image
    image_name = os.path.join(output_folder, f"frame_{frame_number:04d}.jpg")
    cv2.imwrite(image_name, frame)
    frame_number += 1

cap.release()
print(f"✅ Saved {frame_number} images in folder '{output_folder}'")
