import pandas as pd
import matplotlib.pyplot as plt

def Graph(df):
    
    df = df.to_dict('list')

    X = []
    Y1 = []
    Y2 = []

    for i in range(len(df['time'])):
        X.append(df['time'][i].split(":")[1]+':'+df['time'][i].split(":")[2])
        Y1.append(df['temp'][i])
        Y2.append(df['humi'][i])


    flg, gp1 = plt.subplots()

    gp1.plot(X, Y1, 'r-', label='temp')
    gp1.set_xlabel('Time')
    gp1.set_ylabel("Temp")
    gp1.set_ylim(0, 50)


    gp2 = gp1.twinx()
    gp2.plot(X, Y2, 'b-', label='humi')
    gp2.set_ylabel("Humi")
    gp2.set_ylim(0, 50)
    
    plt.grid(True)
    plt.show()

    return

'''
nam = str(input("파일 이름 : "))
df = pd.read_csv(nam + ".csv")


df = df.to_dict('list')

X = []
Y1 = []
Y2 = []

for i in range(len(df['time'])):
    X.append(df['time'][i].split(":")[1]+':'+df['time'][i].split(":")[2])
    Y1.append(df['temp'][i])
    Y2.append(df['humi'][i])


flg, gp1 = plt.subplots()

gp1.plot(X, Y1, 'r-', label='temp')
gp1.set_xlim([0,100])
gp1.set_xlabel('Time')
gp1.set_ylabel("Temp")
gp1.set_ylim(0, 50)


gp2 = gp1.twinx()
gp2.plot(X, Y2, 'b-', label='humi')
gp2.set_ylabel("Humi")
gp2.set_ylim(0, 50)
plt.grid(True)
plt.show()

'''