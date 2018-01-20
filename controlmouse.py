from pynput.mouse import Button , Controller 
import time
mouse = Controller()
mouse.position = (200,30)
for i in range(2):
    time.sleep(1)
    mouse.click(Button.left ,1)