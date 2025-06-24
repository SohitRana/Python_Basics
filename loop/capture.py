import cv2
import os

# Path to your video file
video_path =  "C:\\Users\\Akhil\\Downloads\\00000000700000200 (1).mp4"


# Output folder
output_folder = "C:\\Users\Akhil\\Desktop\\captured_img"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open video file
cap = cv2.VideoCapture(video_path)

# Frame extraction rate (e.g., every 30 frames = approx 1 frame/sec for 30fps video)
frame_interval = 30

frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save every nth frame
    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print("Done.")
