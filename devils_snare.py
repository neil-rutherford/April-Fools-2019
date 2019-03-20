import pyautogui
import time

size = pyautogui.size()
x_min = 0
x_max = (size[0])-1
y_min = 0
y_max = (size[1])-1
pos = pyautogui.position()

def IsMouseMoving():
    a = pyautogui.position()
    time.sleep(0.1)
    b = pyautogui.position()
    if a[0]-b[0] == 0 and a[1]-b[1] == 0:
        return False
    else:
        return True

def SmallerBox():
    global x_min
    global x_max
    global y_min
    global y_max
    x_min += 2
    x_max -= 2
    y_min += 2
    y_max -= 2
    return x_min
    return x_max
    return y_min
    return y_max

def BiggerBox():
    global x_min
    global x_max
    global y_min
    global y_max
    x_min -= 2
    x_max += 2
    y_min -= 2
    y_max += 2
    return x_min
    return x_max
    return y_min
    return y_max

def AdjustXMin():
    global pos
    global x_min
    if pos[0] < x_min:
        pyautogui.moveTo((x_min + 1), None)
    else:
        pass

def AdjustXMax():
    global pos
    global x_max
    if pos[0] > x_max:
        pyautogui.moveTo((x_max - 1), None)
    else:
        pass

def AdjustYMin():
    global pos
    global y_min
    if pos[1] < y_min:
        pyautogui.moveTo(None, (y_min + 1))
    else:
        pass

def AdjustYMax():
    global pos
    global y_max
    if pos[1] > y_max:
        pyautogui.moveTo(None, (y_max - 1))
    else:
        pass

while True:
    IsMouseMoving()
    if IsMouseMoving() == True:
        SmallerBox()
        AdjustXMin()
        AdjustXMax()
        AdjustYMin()
        AdjustYMax()
        print("smaller", x_min, x_max, y_min, y_max)
        time.sleep(0.5)
    elif IsMouseMoving() == False:
        BiggerBox()
        AdjustXMin()
        AdjustXMax()
        AdjustYMin()
        AdjustYMax()
        print("bigger", x_min, x_max, y_min, y_max)
        time.sleep(0.5)
