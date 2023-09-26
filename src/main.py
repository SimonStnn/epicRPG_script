import pyautogui
import time

MOVE_DURATION = .3
TYPE_INTERVAL = .1

# Every x hunts do a /heal
HEAL_INTERVAL = 10

def open_discord():
    pyautogui.moveTo(1900,2100, duration=MOVE_DURATION)
    pyautogui.click()
    pyautogui.moveTo(1900,1900, duration=MOVE_DURATION)
    pyautogui.click()
    
def run_command(command: str, *args: str):
    pyautogui.typewrite(command, interval=TYPE_INTERVAL)
    time.sleep(.5)
    
    for arg in args:
        pyautogui.typewrite("\t\t\t", interval=TYPE_INTERVAL*3)
        time.sleep(.5)
        pyautogui.typewrite(arg, interval=TYPE_INTERVAL)
        time.sleep(.5)
        
    pyautogui.typewrite("\t\n\n", interval=TYPE_INTERVAL*3)
    time.sleep(.5)

open_discord()
while True:
    run_command("/farm")
    for i in range(HEAL_INTERVAL):
        run_command(i)
        run_command("/hunt")
        time.sleep(60)
    run_command("/heal")
    run_command("/mine")