import PIL.Image

targetColor = (255, 0, 0, 255)
black = (0,0,0,255)

def is_similar_color(color1, color2, threshold=200):
    return all(abs(c1 - c2) < threshold for c1, c2 in zip(color1, color2))
def SimplifyImage(img:PIL.Image) -> PIL.Image:
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            current_color = pixels[x, y]
            if is_similar_color(current_color, targetColor):
                pixels[x, y] = targetColor
            else:
                pixels[x, y] = black

    return img


def CaculateHpRatio(image:PIL.Image) -> float:
    img = SimplifyImage(image)
    ratio = 0
    barOffsetX = 0
    HPEndX = 0
    HPWidth = 0
    HPValue = 0

    barOffsetX = CheckBarStart(img)
    HPEndX = CheckHPEnd(img, barOffsetX)

    HPWidth = img.width - 2 * barOffsetX
    HPValue = HPEndX - barOffsetX
    ratio = HPValue/HPWidth

    ratio = round(ratio, 3)

    return ratio

def CheckBarStart(img:PIL.Image) -> int:
    for x in range(img.width):
        checkColor = img.getpixel((x,img.height/2))
        if checkColor == targetColor:
            return x

def CheckHPEnd(img:PIL.Image, offset:int) -> int:
    for x in range(offset, img.width):
        checkColor = img.getpixel((x,img.height/2))
        if checkColor == black:
            return x


'''Test'''
#image = PIL.Image.open("Data/HPBar_test.png")
#SimplizeImage(image)
#print(CaculateHpRatio(image))
#image.save("Data/HPBar.png")