#
# After a post to c.l.py by Richie Hindle:
# http://groups.google.com/groups?th=80e876b88fabf6c9
#
import os
import sys
import ctypes
from ctypes import wintypes
import win32con

byref = ctypes.byref
user32 = ctypes.windll.user32

HOTKEYS = {
    1: (win32con.VK_F4, win32con.MOD_WIN)
}


def handle_win_f4():
    print "Abort key received - Will abort next run - closing checker"
    user32.PostQuitMessage(0)

HOTKEY_ACTIONS = {
    1: handle_win_f4
}

#
# RegisterHotKey takes:
#  Window handle for WM_HOTKEY messages (None = this thread)
#  arbitrary id unique within the thread
#  modifiers (MOD_SHIFT, MOD_ALT, MOD_CONTROL, MOD_WIN)
#  VK code (either ord ('x') or one of win32con.VK_*)
#

print "Loading background process to check for stop signal, press ''Windows key + F4'' to stop the bot on next cycle"
for id, (vk, modifiers) in HOTKEYS.items():
    print "Registering id", id, "for key", vk
    if not user32.RegisterHotKey(None, id, modifiers, vk):
        print "Unable to register id", id

#
# Home-grown Windows message loop: does
#  just enough to handle the WM_HOTKEY
#  messages and pass everything else along.
#

try:
    msg = wintypes.MSG()
    while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            action_to_take = HOTKEY_ACTIONS.get(msg.wParam)
            if action_to_take:
                action_to_take()

    user32.TranslateMessage(byref(msg))
    user32.DispatchMessageA(byref(msg))

finally:
    for id in HOTKEYS.keys():
        user32.UnregisterHotKey(None, id)
