import os

from pynput import keyboard


def on_press(key):
    key_str = "{0}".format(key)
    if key_str == "<179>":
        stream = os.popen("/usr/local/bin/issw")
        output = stream.read().strip()
        if output == "com.apple.keylayout.ABC":
            os.system("/usr/local/bin/issw com.apple.keylayout.Russian")
        else:
            os.system("/usr/local/bin/issw com.apple.keylayout.ABC")


with keyboard.Listener(on_press=on_press, on_release=None) as listener:
    listener.join()
