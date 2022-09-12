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

By default executable will be installed as `/usr/local/bin/issw`

Create fn.py file in ~/. Or clone the repository. 
------------

    import os
    from pynput import keyboard

    def on_press(key):
        key_str = '{0}'.format(key)
        if (key_str == '<179>'):
            stream = os.popen('/usr/local/bin/issw')
            output = stream.read().strip() 
            if (output == 'com.apple.keylayout.ABC'):
                os.system('/usr/local/bin/issw com.apple.keylayout.Russian')
            else:
                os.system('/usr/local/bin/issw com.apple.keylayout.ABC')


    with keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
`<179>` is key code for `fn`. Don't forget to run `issw -l` in terminal to get list of available input sources and modify script above if needed!

Set this to "Do Nothing"
------------
![ezgif-5-aeb126ae5e](https://user-images.githubusercontent.com/33498670/167285047-18f7a509-b56d-4f1f-896a-963c034947dc.jpeg)

Setup auto run of the script every time you log in (python3 should be installed)
------------
1. Install `pynput` python module:
    `/usr/bin/python3 -m pip install pynput`
or, if you are using your own python installation:
    `/your/python3/executable/path -m pip install pynput`
2. Inside `fn.plist` file, change paths to the python executable (if you are using custom python installation) and the script file. Mine is `/Users/norflin/fn.py`. Paths should be full.
3. Copy the plist file to special directory: `cp -R fn.plist ~/Library/LaunchAgents/`.
4. Then run this command: `launchctl load ~/Library/LaunchAgents/fn.plist` - it will tell mac to run this file every time you log in. If you want to stop it run `launchctl unload ~/Library/LaunchAgents/fn.plist` and remove the file `rm -rf ~/Library/LaunchAgents/fn.plist`.
5. Mac might ask you to grant permission for python to monitor input from your keyboard and `Accessibility`. Generally macOS asking about `Input Monitoring`, add your python3 executable to `Accessibility` if no popup with this showed.
6. Restart. Log in. It should work.

P.S. Don't forget to reinstall `pynput` after upgrades.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# RESULT:
You can toggle input source with "fn" button, but without showing the pop up!

