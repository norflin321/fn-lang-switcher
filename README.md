# THE PROBLEM:
![ezgif-5-86271457e6](https://user-images.githubusercontent.com/33498670/167284292-2fe06593-0e47-4c7e-8086-8abd2237466c.gif)

Not only its slow, but when mouse cursor happens to be in the center of the screen, it selects the wrong language for you!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# THE SOLUTION (get rid of the pop up):

Install ["issw"](https://github.com/vovkasm/input-source-switcher) a small utility for macos to switch input sources from a command line.
------------

    git clone https://github.com/norflin321/input-source-switcher.git
    cd input-source-switcher
    mkdir build && cd build
    cmake ..
    make
    make install

Create fn-lang-switcher.py file in ~/.
------------

    import os
    from pynput import keyboard

    def on_press(key):
        key_str = '{0}'.format(key)
        if (key_str == '<179>'):
            stream = os.popen('issw')
            output = stream.read().strip()
            if (output == 'com.apple.keylayout.ABC'):
                os.system('issw com.apple.keylayout.Russian')
            else:
                os.system('issw com.apple.keylayout.ABC')


    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
"<179>" is key code for "fn", run "issw -l" in terminal to get list of available input sources, modify script above if needed

Set this to "Do Nothing"
------------
![ezgif-5-aeb126ae5e](https://user-images.githubusercontent.com/33498670/167285047-18f7a509-b56d-4f1f-896a-963c034947dc.jpeg)

Then run this script on log in (python3 should be installed)
------------
https://stackoverflow.com/a/9523030/16259768

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# RESULT:
You can toggle input source with "fn" button, but without showing the pop up!

