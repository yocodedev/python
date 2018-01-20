from pynput.mouse import Button , Controller 
import time
mouse = Controller()
mouse.position = (1165,280)
'mouse.click(Button.left ,1)'
for i in range(3):
    time.sleep(1)
    mouse.position = (1290,666)
    'mouse.click(Button.left ,1)'
    time.sleep(1)
    mouse.position = (1474,50)
    'mouse.click(Button.left ,1)'
    mouse.position = (1280,550)
    time.sleep(2)
    'time.sleep(1)'
    'mouse.click(Button.left ,1)'