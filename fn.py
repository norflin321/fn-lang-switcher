import os

from pynput import keyboard

COM_APPLE_KEYLAYOUT = "com.apple.keylayout"
ISSW = "/usr/local/bin/issw"


def on_press(inputs: list[str]):
    def handler(key):
        # "<179>" is fn-key
        if str(key) != "<179>":
            return
        stream = os.popen(ISSW)
        output = stream.read().strip()
        current_input_index = inputs.index(output)
        next_index = (current_input_index + 1) % len(inputs)
        next_input = inputs[next_index]
        os.popen(f"{ISSW} {next_input}")

    print(f"Current inputs: [{', '.join(inputs)}]")
    return handler


def list_inputs():
    stream = os.popen(f"{ISSW} -l")
    outputs = stream.read().strip().split("\n")
    inputs = [line for line in outputs if line.startswith(COM_APPLE_KEYLAYOUT)]
    return inputs


if __name__ == "__main__":
    with keyboard.Listener(
        on_press=on_press(list_inputs()), on_release=None
    ) as listener:
        listener.join()
