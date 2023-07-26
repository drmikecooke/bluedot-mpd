from subprocess import run

def MPDstop():
	MPD("stop","Stop MPD and shutdown rpi")
	run(["sudo","shutdown","now"])
	
def MPDpause():
	MPD("pause","Pause MPD")

def MPDplay():
	MPD("play","Play MPD")

def MPD(act,msg):
	print(msg)
	run(__MPD__+[act])

def MPDinit(host):
	global __MPD__
	__MPD__=["mpc",f"--host={host}"]
	run(__MPD__)
