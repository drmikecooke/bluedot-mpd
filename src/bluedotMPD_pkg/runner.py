from bluedot import BlueDot
from signal import pause
from .MPD import MPDinit,MPDstop,MPDpause,MPDplay
from os import environ

def main():
	MPDinit(environ['MPDHOST']) # set by systemd
	bd = BlueDot(rows=3)
	bd[0,0].color="red" # traffic light format
	bd[0,1].color="yellow"
	bd[0,2].color="green"
	bd[0,0].when_pressed=MPDstop
	bd[0,1].when_pressed=MPDpause
	bd[0,2].when_pressed=MPDplay
	pause()
