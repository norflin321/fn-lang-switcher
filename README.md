# THE BUG:
![ezgif-5-86271457e6](https://user-images.githubusercontent.com/33498670/167284292-2fe06593-0e47-4c7e-8086-8abd2237466c.gif)

not only its fucking slow, but when mouse coursor happens to be in the center of the screen, it selects the wrong language for you!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# THE SOLUTION (get rid of the pop up):

Install "issw" a small utility for macos to switch input sources from a command line.
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
        
Then run this python3 script on log in
------------
https://stackoverflow.com/a/9523030/16259768
