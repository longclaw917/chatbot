import pyautogui
from time import sleep


while True:
    sleep(3)
    key = pyautogui.position()
    print(key)