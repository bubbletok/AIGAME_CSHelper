import win32api
import win32con

class AutoClicker():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def click(self, x, y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)


if __name__ == "__main__":
    clicker = AutoClicker()
    clicker.click(0,0)