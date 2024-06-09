import win32gui, win32api

class draw:
    def __init__(self):
        hwnd = win32gui.GetDesktopWindow()
        self.hdc = win32gui.GetDC(hwnd)
    def rect(self, x1, y1, x2, y2, color=(255,0,0)):
        # color = (255,0,0) int type
        color = win32api.RGB(0,255,0) if not color else win32api.RGB(color[0], color[1], color[2])
        for i in range(x1, x2):
            win32gui.SetPixel(self.hdc, i, y1, color)
            win32gui.SetPixel(self.hdc, i, y2, color)
        for j in range(y1, y2):
            win32gui.SetPixel(self.hdc, x1, j, color)
            win32gui.SetPixel(self.hdc, x2, j, color)