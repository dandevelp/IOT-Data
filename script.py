import serial
import json

filelocation = "/var/www/html/data.html"

port = "/dev/ttyACM1"
baud = 9600
 
ser = serial.Serial(port, baud, timeout=1)

x = input('press enter:')
##ser.write('1')
limit = 7
firstrun = True
tempdict = []
ecgdict = []
posdict = []
respdict = []
rsidict = []
conddict = []
voltdict = []

def temp(data):
    if(len(tempdict)< 11):
        tempdict.append(data)
        if(len(tempdict) == 10):
            global limit
            limit -= 1

def ecg(data):
    if(len(ecgdict)< 11):
        ecgdict.append(data)
        if(len(ecgdict) == 10):
            global limit
            limit -= 1

def pos(data):
    if(len(posdict)< 11):
        posdict.append(data)
        if(len(posdict) == 10):
            global limit
            limit -= 1

def resp(data):
    if(len(respdict)< 11):
        respdict.append(data)
        if(len(respdict) == 10):
            global limit
            limit -= 1

def cond(data):
    if(len(conddict)< 11):
        conddict.append(data)
        if(len(conddict) == 10):
            global limit
            limit -= 1

def rsi(data):
    if(len(rsidict)< 11):
        rsidict.append(data)
        if(len(rsidict) == 10):
            global limit
            limit -= 1

def volt(data):
    if(len(voltdict)< 11):
        voltdict.append(data)
        if(len(voltdict) == 10):
            global limit
            limit -= 1

def loopeee():
    line = ser.readline()
    ver = line[:4]
    print(ver)
    print(line)
    s = temp.decode("utf-8")[5:-2]
    if(len(s) != 5):
        print("empty")
    else:
        tempdict.append(s)
        print(s)
        global limit
        limit -= 1
    return

while limit != 0:
    while firstrun == True:
        print(ser.readline())
        print("first")
        firstrun = False
    line = ser.readline().decode('utf-8')
    ver = line[:4]
    if(ver == 'tmp:'):
        data = line[4:-2]
        temp(data)
    elif(ver == 'ecg:'):
        data = line[4:-2]
        ecg(data)
    elif(ver == 'pos:'):
        data = line[4:-2]
        pos(data)
    elif(ver == 'rsp:'):
        data = line[4:-2]
        resp(data)
    elif(ver == 'cnd:'):
        data = line[4:-2]
        cond(data)
    elif(ver == 'rsi:'):
        data = line[4:-2]
        rsi(data)
    elif(ver == 'vlt:'):
        data = line[4:-2]
        volt(data)
    ##print(ver)
    ##print(line)
    ##loopeee()
    ##print(limit)

print(len(tempdict))


with open(filelocation, 'w+') as op:
    jj = json.dumps([{'temp' : temp, 'ecg' : ecg, 'pos' : pos, 'rsp' : rsp, 'cnd' : cnd, 'rsi' : rsi, 'vlt' : vlt} for temp, ecg, pos, rsp, cnd, rsi, vlt in zip(tempdict, ecgdict, posdict, respdict, conddict, rsidict, voltdict)])
    op.write(jj)
