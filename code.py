import win32api, win32con
import ImageGrab
import os
import time

"""

All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Game page is scrolled to the top and game is run in normal mode via the portal (not Facebook)
x_pad = -1
y_pad = 237
Play area =  x_pad+1, y_pad+1, x_pad+1653, y_pad+645
"""

# Globals
# ------------------

x_pad = -1
y_pad = 237


def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1653, y_pad+645)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    pass


if __name__ == '__main__':
    main()


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print "Click."


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print 'left release'


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y