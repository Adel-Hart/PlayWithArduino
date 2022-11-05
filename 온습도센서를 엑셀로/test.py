import serial
import pandas as pd
import time
import keyboard
import graph

data = []



ser = serial.Serial()
ser.port = str(input("포트 선택 : "))
ser.baudrate = int(input("보드레이트 선택 : "))

ser.timeout = 2

ser.open()

data = []

while True:
	
	try:
		humi = ser.readline().split(b', ')[0].decode('utf-8')
		temp = ser.readline().split(b', ')[1].decode('utf-8')
		rst_time = int(ser.readline().split(b', ')[2].decode('utf-8'))

		rst_time = rst_time // 1000

		data.append([time.strftime('%H:%M:%S', time.localtime(time.time())), temp, humi])

		print("Recording...")
		if keyboard.is_pressed("q"):
			break

		time.sleep(rst_time)
	except:
		pass


ser.close()

df = pd.DataFrame(data, columns=['time', 'temp', 'humi']).drop(0).drop(1)

df.to_csv('./'+time.strftime('%Y-%b-%d', time.localtime(time.time()))+'.csv')

graph.Graph(df)
