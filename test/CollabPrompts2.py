#Cell 1
!nvidia-smi





#Cell 2


!pip install ultralytics --quiet
!sudo apt install tesseract-ocr -y
!pip install pytesseract opencv-python --quiet
!pip install openai





#Cell 3

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("/content/DarkPatterns/Pictures/TerpStraight.jpg")
results[0].show()




#Cell 4

import cv2
import pytesseract
from PIL import Image
import re

img = cv2.imread("/content/DarkPatterns/Pictures/TerpStraight.jpg")

text = pytesseract.image_to_string(img)

prices = re.findall(r'\d+[.,]?\d*', text)

if prices:
    max_price = max([float(p.replace(",", ".")) for p in prices])
    print("Highest price detected:", max_price)

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
