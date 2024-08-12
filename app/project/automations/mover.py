import pyautogui as pg
import time
import random

while True:
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    pg.moveTo(x, y, duration=0.25)
    time.sleep(5)
    
    