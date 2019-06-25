import socket
import sys
import json
import time
import datetime
import os
import errno

import socket
from Crypto.PublicKey import RSA
# argv 1 : unit id



def encrypt_datas(data):
    key = RSA.importKey(open('./keys/priv/file-priv.pem').read())
    return key.encrypt(data)

def generateFile(datas, unitId):
    fileDatas = {
        "unitId": unitId,
        "date": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "automate": datas
    }
    print(datas)
    fileName = "datas/"+unitId+"_"+str(int(time.time()))+".json"

    if not os.path.exists(os.path.dirname(fileName)):
        try:
            os.makedirs(os.path.dirname(fileName))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    f = open(fileName, "w+")
    f.write(encrypt_datas(json.dumps(fileDatas)))
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

getDatas = True
if (len(sys.argv) < 2):
    print("Must set a unit number in argv!")
    getDatas = False
elif (len(sys.argv) > 2):
    automateConfig = []
    for i in range(2,len(sys.argv), 3) :
        automateConfig.append({"ip": sys.argv[i], "port": sys.argv[i+1], "id": sys.argv[i+2]})
else:
    with open("automate.json") as automateConfigFile:  
        automateConfig = json.load(automateConfigFile)

while getDatas:
    datas = []
    for automate in automateConfig:
        datas.append(getAutomatData(automate["ip"], automate["port"]))
    print(generateFile(datas, sys.argv[1]))
    time.sleep(60)