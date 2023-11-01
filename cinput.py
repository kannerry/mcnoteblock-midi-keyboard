import keyboard
import mouse

def debug_key_down(event):
	if event.event_type == keyboard.KEY_DOWN:
		if event.name == "up":
			move_mouse(0, -10)
		if event.name == "down":
			move_mouse(0, 10)
		if event.name == "left":
			move_mouse(-10, 0)
		if event.name == "right":
			move_mouse(10, 0)
		if event.name == "home":
			for num in range(60):
				move_mouse(0, -10)

def hook_key_down(_callback):
	keyboard.hook(_callback)

def move_mouse(x = 0, y = 0, time = 0.01):
	mouse.move(x, y, False, time)

if __name__ == "__main__": # test case
	print("// INIT KBINPUT TEST - (f12 exit) //")
	hook_key_down(debug_key_down)
	keyboard.wait("f12")