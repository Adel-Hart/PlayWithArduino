import serial
import os
import webbrowser
import keyboard
import time
from selenium import webdriver

ser = serial.Serial()
ser.port = str(input("포트 선택 : "))
ser.baudrate = int(input("보드레이트 선택 : "))
what = ""

ser.timeout = 2

ser.open()

while True:
    what = ser.readline().decode('utf-8')
    if keyboard.is_pressed("q"):
        break
    if keyboard.is_pressed("s"):
        print('set')
        ser.write('s'.encode())
    if keyboard.is_pressed("g"):
        print('go')
        ser.write('g'.encode())



    if "BOOM" in what:
        os.system('taskkill /f /im chrome.exe')
        driver = webdriver.Chrome()
        driver.get("https://www.ebsi.co.kr/ebs/lms/lmsx/retrieveSbjtDtl.ebs?courseId=S20210000194")
        time.sleep(100)

    print(what)
    time.sleep(0.1)
    