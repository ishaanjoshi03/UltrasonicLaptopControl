import pyautogui, time

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

time.sleep(2)

pyautogui.click()          # Click the mouse.

time.sleep(2)

pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
#pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

time.sleep(2)

pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.

time.sleep(2)

pyautogui.doubleClick()    # Double click the mouse.

time.sleep(2)

pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

time.sleep(2)

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key

time.sleep(2)

pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

pyautogui.keyDown('shift') # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
pyautogui.keyUp('shift')   # Let go of the Shift key.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.