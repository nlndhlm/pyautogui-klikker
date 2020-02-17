import pyautogui
import time

antall_klikk = 10
delay = 1

pyautogui.FAILSAFE = True

k = 0

while k < antall_klikk:
    pyautogui.click()
    print("Klikk nummer ", k)
    time.sleep(delay)

    k = k + 1

