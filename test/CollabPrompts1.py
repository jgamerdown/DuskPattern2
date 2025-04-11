#Cell 1

# GPU Check
!nvidia-smi





#Cell 2

# Install YOLOv8
!pip install ultralytics --quiet

# Install pytesseract
!sudo apt install tesseract-ocr -y
!pip install pytesseract opencv-python --quiet

# (Optional) If you have a languagemodels module
!pip install openai





#Cell 3

from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # or yolov8n.pt if you're testing
results = model("/content/DarkPatterns/Pictures/TerpStraight.jpg")  # Or your uploaded image
results[0].show()  # Display detection result




#Cell 4

import cv2
import pytesseract
from PIL import Image
import re

# Load image
img = cv2.imread("/content/DarkPatterns/Pictures/TerpStraight.jpg")

# Use pytesseract directly to get raw text
text = pytesseract.image_to_string(img)

# Extract price-like patterns using regex
prices = re.findall(r'\d+[.,]?\d*', text)

# Convert and compare
if prices:
    max_price = max([float(p.replace(",", ".")) for p in prices])
    print("Highest price detected:", max_price)

    # Compare with stored value
    try:
        with open("high.txt", "r") as f:
            old = float(f.read())
    except:
        old = 0

    if max_price > old:
        with open("high.txt", "w") as f:
            f.write(str(max_price))
        print("New highest price updated.")
    else:
        print("No update needed.")
else:
    print("No prices detected.")
