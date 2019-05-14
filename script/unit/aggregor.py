import socket
import sys
import json
import time
import datetime

import socket

# argv 1 : unit id

def generateFile(datas, unitId):
    fileDatas = {
        "unitId": unitId,
        "date": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "automate": datas
    }
    fileName = "datas/"+unitId+"_"+str(int(time.time()))+".json"
    f = open(fileName, "w+")
    f.write(json.dumps(fileDatas))
    f.close()
    return fileName

def getAutomatData(ip, port):
    try:
        socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Get "+ip+" "+port)
        socketClient.connect((ip, int(port)))
        if socketClient:
            data = socketClient.recv(9999999)
            socketClient.close()
            return json.loads(data)   
    except socket.error:
        return json.loads("{}")
    return json.loads("{}")

if not (len(sys.argv) == 2):
    print("Must set a unit number in argv!")
else:
    with open("automate.json") as automateConfigFile:  
        automateConfig = json.load(automateConfigFile)
    getDatas = True
    while getDatas:
        datas = []
        for automate in automateConfig:
            datas.append(getAutomatData(automate["ip"], automate["port"]))
        print(generateFile(datas, sys.argv[1]))
        time.sleep(10)