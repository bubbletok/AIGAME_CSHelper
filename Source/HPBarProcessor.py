import PIL.Image
from MinionsException import *

targetColor = (255, 0, 0)
black = (0,0,0)

def is_similar_color(color1, color2, threshold=200):
    return all(abs(c1 - c2) < threshold for c1, c2 in zip(color1, color2))

def SimplifyImage(img:PIL.Image) -> PIL.Image:
    bar = HPBarOutliner(img)
    pixels = bar.load()

    for y in range(bar.height):
        for x in range(bar.width):
            current_color = pixels[x, y]
            if is_similar_color(current_color[0:3], targetColor):
                pixels[x, y] = targetColor
            else:
                pixels[x, y] = black

    #bar.show()
    
    return bar

def HPBarOutliner(img:PIL.Image) -> PIL.Image:
    pixels = img.load()

    # hpbar outline
    for y in range(img.height):
        for x in range(img.width):
            current_color = pixels[x, y]
            if is_similar_color(current_color[0:3], black, 50):
                pixels[x, y] = black
    #img.show()

    hpbarTopLeft = FindTopLeft(img)
    hpbarBottomRight = FindBottomRight(img)
    
    #print(hpbarTopLeft)
    #print(hpbarBottomRight)

    # crop img using outline
    try:
        result = img.crop((hpbarTopLeft[0], hpbarTopLeft[1], hpbarBottomRight[0]+1, hpbarBottomRight[1]+1))
    except Exception as e:
        print(e)

    #result.show()

    return result

def FindTopLeft(img:PIL.Image) -> list[int,int]:
    pixels = img.load()
    count = 0
    result = (0,0)

    for y in range(img.height):
        for x in range(img.width):
            if count > img.width/2:
                return result
            current_color = pixels[x, y]
            if current_color[0:3] == black:
                if count == 0:
                    result = (x,y)
                count += 1
            elif current_color[0:3] != black and count < img.width/2:
                count = 0
    
    raise PixelNotFound()

def FindBottomRight(img:PIL.Image) -> list[int,int]:
    pixels = img.load()
    count = 0
    result = (0,0)

    for y in range(img.height-1, -1, -1):
        for x in range(img.width-1, -1, -1):
            if count > img.width/2:
                return result
            current_color = pixels[x,y]
            if current_color[0:3] == black:
                if count == 0:
                    result = (x,y)
                count += 1
            elif current_color[0:3] != black and count < img.width/2:
                count = 0

    raise PixelNotFound()

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
        if checkColor[0:3] == targetColor:
            return x

    return 0

def CheckHPEnd(img:PIL.Image, offset:int) -> int:
    for x in range(offset, img.width):
        checkColor = img.getpixel((x,img.height/2))
        if checkColor[0:3] == black:
            return x

    return img.width

'''Test'''
if __name__ == '__main__':
    test = PIL.Image.open("Data/HPBar_test6.png")
    crop = SimplifyImage(test)
    crop.show()
    print(CaculateHpRatio(test))