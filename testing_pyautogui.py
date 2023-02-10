import pyautogui
import time
import serial

ArduinoSerial = serial.Serial('/dev/cu.usbmodem14201', 9600)
time.sleep(2)

""" incoming = str (ArduinoSerial.readline())
print(incoming) """

while 1 == 1:
    incoming = str (ArduinoSerial.readline())
    print(incoming)
    if "ahs" in incoming:
        pyautogui.click(1302, 481)

        pyautogui.keyDown('command')
        pyautogui.press('t')
        pyautogui.keyUp('command')

        pyautogui.typewrite('https://ahs-fusd-ca.schoolloop.com/portal/student_home')

        time.sleep(1)

        pyautogui.press('enter')
        

    if 'Vup' in incoming:
        pyautogui.hotkey('up')

    if 'Vdown' in incoming:
        pyautogui.hotkey('down')

    if 'Rewind' in incoming:
        pyautogui.hotkey('left')