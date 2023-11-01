import mido
import mouse
import time
from cinput import move_mouse

_BIN_MESSAGE_CLOCK = bytearray(b'\xf8')

def special_case_move(x, y):
	move_mouse(x, y, 0)
	time.sleep(0.03)

def move_and_play(x, y):
	move_mouse(x, y, 0)
	time.sleep(0.03)
	mouse.click()
	time.sleep(0.06)
	move_mouse(-x, -y, 0)
	time.sleep(0.01)

def ang_to_pix(ang_num):
	div_num = ang_num / 1.5 # -45 / 1.5 = -30
	pixel_num = div_num * 10 # -30 * 10 = -300
	return pixel_num

def hook_midi(_callback = None):
	with mido.open_input() as open_input:
		for msg in open_input:
			_callback(msg)

def debug_hook(msg):
	print(msg, msg.bin())

def play_note(num):
	match num:
		case 54:
			move_and_play(ang_to_pix(-36), ang_to_pix(9))
		case 55:
			move_and_play(ang_to_pix(-24), ang_to_pix(9))
		case 56:
			move_and_play(ang_to_pix(-15), ang_to_pix(9))
		case 57:
			move_and_play(ang_to_pix(15), ang_to_pix(9))
		case 58:
			move_and_play(ang_to_pix(24), ang_to_pix(9))
		case 59:
			move_and_play(ang_to_pix(36), ang_to_pix(9))
		case 60:
			move_and_play(ang_to_pix(-54), ang_to_pix(9))
		case 61:
			move_and_play(ang_to_pix(-45), ang_to_pix(12))
		case 62:
			move_and_play(ang_to_pix(-21), ang_to_pix(15))
		case 63:
			move_and_play(ang_to_pix(21), ang_to_pix(15))
		case 64:
			move_and_play(ang_to_pix(45), ang_to_pix(12))
		case 65:
			move_and_play(ang_to_pix(55), ang_to_pix(9))
		case 66:
			move_and_play(ang_to_pix(-66), ang_to_pix(12))
		case 67:
			move_and_play(ang_to_pix(-60), ang_to_pix(15))
		case 68:
			move_and_play(ang_to_pix(-28), ang_to_pix(28))
		case 69:
			move_and_play(ang_to_pix(28), ang_to_pix(28))
		case 70:
			move_and_play(ang_to_pix(60), ang_to_pix(15))
		case 71:
			move_and_play(ang_to_pix(66), ang_to_pix(12))
		case 72:
			move_and_play(ang_to_pix(-90), ang_to_pix(12))
		case 73:
			move_and_play(ang_to_pix(-90), ang_to_pix(15))
		case 74:
			move_and_play(ang_to_pix(-90), ang_to_pix(33))
		case 75:
			move_and_play(ang_to_pix(90), ang_to_pix(33))
		case 76:
			move_and_play(ang_to_pix(90), ang_to_pix(15))
		case 77:
			move_and_play(ang_to_pix(90), ang_to_pix(12))
		case 78:
			special_case_move(ang_to_pix(90), ang_to_pix(9))
			move_and_play(ang_to_pix(90), ang_to_pix(9))
			special_case_move(ang_to_pix(-90), ang_to_pix(-9))

if __name__ == "__main__": # test case
	print("// INIT MIDI TEST //")
	hook_midi(debug_hook)