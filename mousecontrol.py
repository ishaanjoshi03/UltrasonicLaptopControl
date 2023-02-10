import pyautogui, serial, time

ArduinoSerial = serial.Serial('/dev/cu.usbmodem14201', 9600)
time.sleep(2)


while True:
    incoming = str(ArduinoSerial.readline())

    if incoming == "Start":
        print("Started")
        currentMouseX, currentMouseY = pyautogui.position()
        #print(currentMouseX)
        currentMouseX = float(currentMouseX)
        currentMouseY = float(currentMouseY)
        screenx = currentMouseX / 1440
        screeny = currentMouseY / 900

        while True:
            if "x" in ArduinoSerial.readline():    
                newX = ArduinoSerial.readline() * 1440 / 90
                pyautogui.moveTo(currentMouseX + newX, currentMouseY)
            elif "y" in ArduinoSerial.readline():
                newY = ArduinoSerial.readline() * 900 / 90
                pyautogui.moveTo(currentMouseX, currentMouseY + newY)
