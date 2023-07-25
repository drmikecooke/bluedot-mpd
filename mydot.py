from bluedot import BlueDot
from subprocess import run
from signal import pause

def MPDstop():
	print("Stop MPD action here and shutdown rpi")
	run(cmd+["stop"])
	run(["sudo","shutdown","now"])
	
def MPDpause():
	print("Pause MPD action here")
	run(cmd+["pause"])

def MPDplay():
	print("Play MPD action here")
	run(cmd+["play"])

cmd=["mpc",f"--host={input('Host: ')}"]

run(cmd)
	
bd = BlueDot(rows=3)
bd[0,0].color="red"
bd[0,1].color="yellow"
bd[0,2].color="green"
bd[0,0].when_pressed=MPDstop
bd[0,1].when_pressed=MPDpause
bd[0,2].when_pressed=MPDplay
pause()
