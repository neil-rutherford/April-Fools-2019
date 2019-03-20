import pyautogui
import random
import time

size = pyautogui.size()
x_min = 0
x_max = (size[0])-1
y_min = 0
y_max = (size[1])-1

def ran_pos():
    global x_min
    global x_max
    global y_min
    global y_max
    pyautogui.moveTo((random.randint(x_min,x_max), random.randint(y_min,y_max)))

while True:
    ran_pos()
    time.sleep(random.randint(0,10))
    print('runnin')
