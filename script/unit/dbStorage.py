import mysql.connector
import time
import json
import sys
from os import listdir
import os

class NoUnitFind(Exception):
    pass

class NoInsertDo(Exception):
    pass

class NoUnitRecordInsert(Exception):
    pass

def run():
    if len(sys.argv) < 5:
        print('Need args : dbUrl username password port')

    listen = True
    while listen:
        for fileName in listdir("datas"):
            with open('datas/'+fileName, 'r') as content_file:
                fileContent = json.loads(content_file.read())
            try:
                dbWrite(fileContent, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
                os.remove('datas/'+fileName)
            except NoInsertDo:
                print('Error Insert unit')
        time.sleep(2)

def dbWrite(fileContent, host, user, passwd, port):
    mydb = mysql.connector.connect(host=host, user=user, passwd=passwd, port=port)
    try:
        unitId = getUnitId(fileContent["unitId"], mydb)
        creatingDate = fileContent['date']
        unitRecordId = insertUnitRecord(mydb, unitId, creatingDate)
        for automateDatas in fileContent["automate"]:
            insertAutomateRecording(mydb, unitRecordId, automateDatas)
    except NoUnitFind:
        print('No unit find in DB for '+fileContent["unitId"])
        raise NoInsertDo()
    except NoUnitRecordInsert:
        print('No unit recorde rcv after insert!')

def getUnitId(unitNumber, mydb):
    requestor = mydb.cursor()
    useDb(requestor)
    requestor.execute("SELECT id FROM `unit` WHERE number="+unitNumber)
    datas = requestor.fetchall()
    if len(datas) <= 0:
        raise NoUnitFind()
    return datas[0][0]

def useDb(request):
    request.execute("use au_bon_beurre")

def insertAutomateRecording(mydb, unitRecordId, datas):
    requestor = mydb.cursor()
    try:
        sql = "INSERT INTO automate_recording (`automate_id`,`unit_recording_id`,`tank_temperature`,`external_temperature`,`milk_tank_weight`,`final_product_weight`,`ph_measurement`,`k_pos_measurement`,`na_cl_concentration`,`salmonella_level`,`e_coli_level`,`listeria_level`) VALUES ("+str(datas["automatId"])+","+str(unitRecordId)+","+str(datas["tankTemperature"])+","+str(datas["externalTemperature"])+","+str(datas["milkTankWeight"])+","+str(+datas["finalProductWeight"])+","+str(datas["phMeasurement"])+","+str(datas["kPosMeasurement"])+","+str(datas["naClConcentration"])+","+str(datas["salmonellaLevel"])+","+str(datas["eColiLevel"])+","+str(datas["listeriaLevel"])+")"
        requestor.execute(sql)
        mydb.commit()
    except:
        print('#############""')
        print(datas)
        print('#############""')
        print(sys.exc_info())

def insertUnitRecord(mydb, unitId, date):
    requestor = mydb.cursor()
    useDb(requestor)
    sql = "INSERT INTO unit_recording (unit_id, record_date) VALUES (%s, %s)"
    val = (unitId, date)
    requestor.execute(sql, val)
    mydb.commit()
    requestor2 = mydb.cursor()
    request = "SELECT id FROM `unit_recording` WHERE unit_id="+str(unitId)+" and record_date=\""+str(date)+"\""
    requestor2.execute(request)
    datas = requestor2.fetchall() 
    if len(datas) <= 0:
        raise NoUnitRecordInsert()
    return datas[0][0]
run()