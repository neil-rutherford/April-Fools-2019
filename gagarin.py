import pyautogui
import numpy as np
import time

time.sleep(1961)
CursPos = pyautogui.position()

while True:
    for Angle in range(0,361):
        x = CursPos[0] + 100 * np.cos(Angle)
        y = CursPos[1] + 100 * np.sin(Angle)
        pyautogui.moveTo(x,y)
