from cmidi import *
from cmidi import _BIN_MESSAGE_CLOCK
from cinput import *
from cutil import *

_KEY_TO_WAIT_FOR = "f12"
_KEY_TO_BREAK_ON = "end"

last_key_played = ""

def keyboard_init(e):
	if e.event_type != keyboard.KEY_DOWN: return
	if e.name == _KEY_TO_WAIT_FOR: 
		init()

def init():
	set_gamemode("survival")
	center_screen(csv(0.0, 90.0))
	hook_midi(midi_interpreter)

def midi_interpreter(midi_message):
	if midi_message.type != "note_on": return
	if midi_message.velocity == 0: return
	if midi_message.note not in range(54, 79):
		print("// NOTE PLAYED NOT IN RANGE //")
		return
	play_note(midi_message.note)

if __name__ == "__main__":
	_dir = grab_direction()
	print("Hop into the minecart, then hop out. This will ensure you're in the correct starting position.")
	time.sleep(0.5)
	print(f'Then, make sure your in-game "Facing" property (in the [F3] menu) shows {get_dir_start_angle(_dir)}.\nFinally, press [F12] once you have done this setup.')
	time.sleep(0.5)
	hook_key_down(keyboard_init)
	keyboard.wait(_KEY_TO_BREAK_ON)