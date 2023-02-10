from serial import Serial
import time
import pyautogui

ArduinoSerial = Serial('/dev/cu.usbmodem14201', 9600)
time.sleep(2)

while True:
    incoming = str (ArduinoSerial.readline())
    print(incoming)

    # if "Play/Pause" in incoming:
        # pyautogui.typewrite(['Space'], 0.2)

    if 'Vup' in incoming:
        pyautogui.hotkey('up')
    
    if 'Vdown' in incoming:
        pyautogui.hotkey('down')
        
    if 'Rewind' in incoming:
        pyautogui.hotkey('left')  