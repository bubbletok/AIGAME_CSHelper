import cv2
import pyscreenshot as ImageGrab
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
def text_recognition(x1,y1,x2,y2):
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1,y1,x2,y2))), cv2.COLOR_BGR2RGB)
    img2char = pytesseract.image_to_string(image, config=custom_config)

    return img2char
