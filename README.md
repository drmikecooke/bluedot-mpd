# bluedot-mpd
Use python bluedot to start/stop/pause music player daemon running on an ancient raspberry pi (rpi) with usb bluetooth dongle for travel use (absent wifi MALP connection).

## Install

I used:

```
pipx install .
```

run in the cloned bluedot-mpd directory. This took a long time on the final, very old rpi Model B Rev 2 (000e revision code from cpuinfo). I would probably run in verbose mode in future.

```
pipx install --verbose .
```

Also, since pip didn't seem to be installed on the lite version of the rpi OS, installing pipx was a bit of a palaver (and again slow):

```
sudo apt install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

The last step sets up a local directory (~/.local/bin) where pipx places links to its application links.

The bdotMPD app can be launched manually at the command line:

```
bdotMPD &
```

The "&" puts the process in background, so you can do other stuff, and sets up a server. You should see what mpd is playing (oh, by the way, the code assumes that you have installed mpc, using "sudo apt install mpc").

The bluedot app with a paired device running the app (Android (this has been tested by me), or 2nd rpi "Desktop" (not tried), see [Getting started](https://bluedot.readthedocs.io/en/latest/gettingstarted.html) and [Android](https://bluedot.readthedocs.io/en/latest/pairpiandroid.html)/[rpi](https://bluedot.readthedocs.io/en/latest/pairpipi.html) pairing sections of the documentation) shows a traffic light of red/yellow/green. Pressing these stops (careful, this also shuts off the mpd rpi), pauses, or plays music on the mpd, respectively. I hope these colours are sort of obvious/intuitive.

There are ways to allow you to exit from the console, which I could go into but won't. Instead . . .

## Systemd

Many "services" that are launched in the background and at startup on Debian-based systems are handled through "systemd". How to put my little app into systemd was a new experience for me, so I will go through the steps derived from the relevant link below.

First:

```
mkdir -p ~/.config/systemd/user
```

This will create a suitable directory for the systemd files in your home directory.


## Learning

### pipx

https://pypa.github.io/pipx/

### Bluedot

https://bluedot.readthedocs.io/en/latest/index.html

### Systemd

https://github.com/torfsen/python-systemd-tutorial
