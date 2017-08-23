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
    screenGrab()


if __name__ == '__main__':
    main()
