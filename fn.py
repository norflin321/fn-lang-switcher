import os

from pynput import keyboard


def on_press(key):
    # "<179>" is fn-key
    if str(key) != "<179>":
        return
    stream = os.popen("/usr/local/bin/issw")
    output = stream.read().strip()
    if output == "com.apple.keylayout.ABC":
        os.system("/usr/local/bin/issw com.apple.keylayout.Russian")
    else:
        os.system("/usr/local/bin/issw com.apple.keylayout.ABC")


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
