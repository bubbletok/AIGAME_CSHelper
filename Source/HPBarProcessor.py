import PIL.Image

targetColor = (255, 0, 0, 255)
black = (0,0,0,255)

def is_similar_color(color1, color2, threshold=200):
    return all(abs(c1 - c2) < threshold for c1, c2 in zip(color1, color2))

def SimplifyImage(img:PIL.Image) -> PIL.Image:
    bar = HPBarOutliner(img)
    pixels = bar.load()

    for y in range(bar.height):
        for x in range(bar.width):
            current_color = pixels[x, y]
            if is_similar_color(current_color, targetColor):
                pixels[x, y] = targetColor
            else:
                pixels[x, y] = black

    return bar

def HPBarOutliner(img:PIL.Image) -> PIL.Image:
    pixels = img.load()

    # hpbar outline
    for y in range(img.height):
        for x in range(img.width):
            current_color = pixels[x, y]
            if is_similar_color(current_color, black, 20):
                pixels[x, y] = black

    hpbarTopLeft = FindTopLeft(img)
    hpbarBottomRight = FindBottomRight(img)
    
    #print(hpbarTopLeft)
    #print(hpbarBottomRight)

    result = img.crop((hpbarTopLeft[0], hpbarTopLeft[1], hpbarBottomRight[0]+1, hpbarBottomRight[1]+1))

    return result

def FindTopLeft(img:PIL.Image) -> list[int,int]:
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            current_color = pixels[x, y]
            if current_color == black[0:3]:
                return (x,y)
def FindBottomRight(img:PIL.Image) -> list[int,int]:
    pixels = img.load()

    for y in range(img.height-1, -1, -1):
        for x in range(img.width-1, -1, -1):
            current_color = pixels[x,y]
            if current_color == black[0:3]:
                return (x,y)

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
        if checkColor == targetColor[0:3]:
            return x

def CheckHPEnd(img:PIL.Image, offset:int) -> int:
    for x in range(offset, img.width):
        checkColor = img.getpixel((x,img.height/2))
        if checkColor == black[0:3]:
            return x


'''Test'''
test = PIL.Image.open("Data/HPBar_test.png")
crop = SimplifyImage(test)
#crop.show()
print(CaculateHpRatio(crop))
crop.save("Data/HPBar_processed.png")