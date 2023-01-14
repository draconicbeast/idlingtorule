import pyautogui
import keyboard
pyautogui.PAUSE = .01
while True:
    pyautogui.screenshot("new.png", region=(2563, 1707, 595, 67))
    if pyautogui.locate("idle_test.png", "new.png") != None and pyautogui.locate ("Fail.png", "new.png") == None:
        pyautogui.click(2750,1903)
    elif pyautogui.locate("idle_test.png", "new.png") != None: print("why")
    elif pyautogui.locate ("Fail.png", "new.png") == None: print("because")
    if keyboard.is_pressed("|"):
        exit()
    print("cheese")