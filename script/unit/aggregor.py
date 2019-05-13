import socket
import sys
import json
import time

import socket


def generateFile(datas, unitId):
    fileName = "datas/"+unitId+"_"+str(time.time())+".json"
    f = open(fileName, "w+")
    f.write(str(datas))
    f.close()
    return fileName

def getAutomatData(ip, port):
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((ip, int(port)))
    if socketClient:
        data = socketClient.recv(9999999)
        socketClient.close()
        return data   
    return "{}"

if not (len(sys.argv) == 2):
    print("Must set a unit number and ipFile.json in argv!")
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