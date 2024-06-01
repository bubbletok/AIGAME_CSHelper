from PIL import Image

image = Image.open("Data/HPBar_test.png")

hpBar = image.resize((1000,100))
pixels = hpBar.load()

def is_similar_color(color1, color2, threshold=200):
    return all(abs(c1 - c2) < threshold for c1, c2 in zip(color1, color2))

targetColor = (255, 0, 0, 255)
black = (0,0,0,255)

barOffsetX = 0
hpBarEndX = 0
hpBarWidth = 0
hpBarValue = 0
hpBarRatio = 0

for y in range(hpBar.height):
    for x in range(hpBar.width):
        current_color = pixels[x, y]
        if is_similar_color(current_color, targetColor):
            pixels[x, y] = targetColor
        else:
            pixels[x, y] = black

for x in range(hpBar.width):
    checkColor = hpBar.getpixel((x,hpBar.height/2))
    if checkColor == targetColor:
        #print(x)
        barOffsetX = x
        break

for x in range(barOffsetX, hpBar.width):
    checkColor = hpBar.getpixel((x,hpBar.height/2))
    if checkColor == black:
        #print(x)
        hpBarEndX = x
        break

hpBarWidth = hpBar.width - 2*barOffsetX
hpBarValue = hpBarEndX - barOffsetX
hpBarRatio = hpBarValue/hpBarWidth
print(hpBarRatio)

hpBar.save("Data/HPBar.png")