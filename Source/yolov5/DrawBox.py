from win32 import win32gui, win32api
import math
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class drawer:
    def __init__(self):
        hwnd = win32gui.GetDesktopWindow()
        self.hdc = win32gui.GetDC(hwnd)
        self.window_rect = win32gui.GetWindowRect(hwnd)
        print(self.window_rect)
    def rect(self, x, y, w, h, _color=(255, 0, 0)):
        # color = (255,0,0) int type
        color = win32api.RGB(_color[0], _color[1], _color[2])
        x, y, w, h = map(math.floor, (x, y, w, h))
        for i in range(x, x + w):
            win32gui.SetPixel(self.hdc, i, y, color)
            win32gui.SetPixel(self.hdc, i, y + h, color)
        for j in range(y, y + h):
            win32gui.SetPixel(self.hdc, x, j, color)
            win32gui.SetPixel(self.hdc, x + w, j, color)

if __name__ == "__main__":
    d = drawer()
    while(1):
        d.rect(10.5, 20.5, 100.7, 50.3)