def text_recognition(x1,y1,x2,y2):

    image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1,y1,x2,y2))), cv2.COLOR_BGR2RGB)
    img2char = pytesseract.image_to_string(image)

    return img2char
