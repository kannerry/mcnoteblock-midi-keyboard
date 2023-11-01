from cinput import *
import time

def set_gamemode(str_mode):
	keyboard.press_and_release("t")
	time.sleep(0.1)
	keyboard.write("/gamemode " + str_mode)
	time.sleep(0.1)
	keyboard.press_and_release("enter")

def csv(yaw, pitch): # values needed to get to a 'centered screen'; center screen values
	rot_p = pitch / 1.5
	rot_y = yaw / 1.5
	return rot_y, rot_p

def center_screen(_center_screen_values):
	amt_y, amt_p = _center_screen_values
	for _ in range(int(amt_p) + 1):
		move_mouse(0, -10 * get_normalized_num(amt_p), 0.01)

def get_normalized_num(_num):
	if _num > 0:
		return 1
	elif _num < 0:
		return -1
	else:
		return 0

def grab_direction():
	dir_input = input("What direction are you facing, when you look towards the noteblocks that have a 1 block seperation?\n(north/south/east/west): ").lower()
	if "north" == dir_input or "south" == dir_input or "east" == dir_input or "west" == dir_input:
		return dir_input
	else:
		print("Input must be north/south/east/west.")
		grab_direction()

def get_dir_start_angle(_dir):
	match _dir:
		case "north":
			return "(180.0 / 90.0)"
		case "south":
			return "(-0.0 / 90.0)"
		case "east":
			return "(-90.0 / 90.0)"
		case "west":
			return "(90.0 / 90.0)"

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

if __name__ == "__main__": # test case
	print("// INIT UTIL TEST (csv()) //")
	print(csv(0, -90))
	print(csv(0, 90))
	print(csv(-90, 1.5))
	print(csv(-45, 3))
