import cv2
import os
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
FRAME_SIZE = 100  # Width of ASCII frame

def resize_image(image, new_width=FRAME_SIZE):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)  # 0.5 adjusts for ASCII aspect
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_frame_to_ascii(image):
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    width = image.width
    ascii_image = "\n".join([ascii_str[i:(i + width)] for i in range(0, len(ascii_str), width)])
    return ascii_image

def convert_video_to_ascii(video_path, output_folder="ascii_frames"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert OpenCV frame (BGR) to PIL image (RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame)
        
        ascii_art = convert_frame_to_ascii(pil_image)

        # Save ASCII frame to text file
        with open(f"{output_folder}/frame_{frame_count}.txt", "w") as f:
            f.write(ascii_art)
        
        print(f"Processed frame {frame_count}")
        frame_count += 1

    cap.release()
    print("Conversion complete! ASCII frames saved in:", output_folder)

# Run the function
video_path = "rabbit hole.mp4"  # Replace with your video file path
convert_video_to_ascii(video_path)
