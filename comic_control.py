import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('/dev/cu.usbmodem14201', 9600)
time.sleep(2)

while 1:
    incoming = str (ArduinoSerial.readline())
    print(incoming)

    # if "Play/Pause" in incoming:
        # pyautogui.typewrite(['Space'], 0.2)

    if 'Vup' in incoming:
        # pyautogui.hotkey('up')
        pyautogui.keyDown('up')
    
    elif 'Vdown' in incoming:
        # pyautogui.hotkey('down')
        pyautogui.keyDown('down')
        
    elif 'Rewind' in incoming:
        pyautogui.hotkey('left')
    else:
        pyautogui.keyUp('up')
        pyautogui.keyUp('down')