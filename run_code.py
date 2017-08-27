import win32api
import win32con
import ImageGrab
import ImageOps
import os
import time
from numpy import *

"""

All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Game page is scrolled to the top and game is run in normal mode via the portal (not Facebook)
There is one line of "news" at the top of the game (In the yellow bar)
x_pad = -1
y_pad = 237
Play area =  x_pad+1, y_pad+1, x_pad+1653, y_pad+645
"""

##########################
# -------Settings------- #
##########################

# Choose your destination. options are 1,2,3,4 which are the options from left to right I.E. 1 is 5 min journey
# Setting this to a number that is not 2, 3, will default to 1
destination = 2
#########################
# -----Settings End----- #
##########################

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
    startGame()


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


class Cord:
    s_train1 = (1483, 406)
    s_train2 = (1452, 433)
    s_train3 = (1436, 446)
    s_train4 = (1400, 465)
    s1 = (561, 528)
    s2 = (744, 538)
    s3 = (919, 538)
    s4 = (1098, 538)
    dock_indicator = (94, 103)
    d_train1 = (1442, 437)
    d_train2 = (1442, 454)
    d_train3 = (1442, 467)
    home_button = (57, 606)
    supply_close_button = (828, 437)
    whistle_button = (36, 320)


def startGame():
    # click top train
    mousePos(Cord.s_train1)
    leftClick()
    time.sleep(.1)

    # click second train
    mousePos(Cord.s_train2)
    leftClick()
    time.sleep(.1)

    # click third train
    mousePos(Cord.s_train3)
    leftClick()
    time.sleep(.1)

    # click fourth train
    mousePos(Cord.s_train4)
    leftClick()
    time.sleep(.1)

    if destination is 2:
        # s2 destination
        mousePos(Cord.s2)
        leftClick()
        time.sleep(.1)
    if destination is 3:
        # s3 destination
        mousePos(Cord.s3)
        leftClick()
        time.sleep(.1)
    if destination is 4:
        # s4 destination
        mousePos(Cord.s4)
        leftClick()
        time.sleep(.1)
    else:
        # s1 destination
        mousePos(Cord.s1)
        leftClick()
        time.sleep(.1)


if __name__ == '__main__':
    main()
