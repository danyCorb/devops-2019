import mysql.connector
import time
import json
from os import listdir
import os

class NoUnitFind(Exception):
    pass

class NoInsertDo(Exception):
    pass

def run():
    listen = True
    while listen:
        for fileName in listdir("datas"):
            with open('datas/'+fileName, 'r') as content_file:
                fileContent = json.loads(content_file.read())
                try:
                    dbWrite(fileContent)
                    os.remove('datas/'+fileName)
                except NoInsertDo:
                    print('Error Insert unit')
        time.sleep(1)

def dbWrite(fileContent):
    mydb = mysql.connector.connect(host="dany-corbineau.ddns.net", user="corentin.dupont", passwd="dupont.corentin", port="8001")
    try:
        unitId = getUnitId(fileContent["unitId"], mydb)
        creaingDate = fileContent['date']
        unitRecordId = insertUnitRecord(mydb, unitId, creatingDate)
        for automateDatas in fileContent["automate"]:
            automatId = getAutomatId(mydb, automateDatas["automatId"], unitId)
            insertAutomateRecording(mydb, unitId, automatId, automateDatas)
    except NoUnitFind:
        print('No unit find in DB for '+fileContent["unitId"])
        raise NoInsertDo()
        

def getUnitId(unitNumber, mydb):
    requestor = mydb.cursor()
    useDb(requestor)
    requestor.execute("SELECT id FROM `unit` WHERE number="+unitNumber)
    datas = requestor.fetchall()
    if len(datas) <= 0:
        raise NoUnitFind()
    return datas[0]

def useDb(request):
    request.execute("use au_bon_beurre")

def getAutomatId(mydb, automatNumber, unitId):
    requestor = mydb.cursor()
    useDb(requestor)
    requestor.execute("SELECT id FROM `automate` WHERE number="+automatNumber+' and unit_id='+unitId)
    datas = requestor.fetchall()
    return datas[0]

def insertAutomateRecording(mydb, unitId, automatId, datas):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]
    requestor.executemany(sql, val)
    mydb.commit()

def insertUnitRecord(mydb, unitId, date):
    requestor = mydb.cursor()
    useDb(requestor)
    sql = "INSERT INTO unit_recording (unit_id, record_date) VALUES (%s, %s)"
    val = (unitId, date)
    requestor.execute(sql, val)
    mydb.commit()
    requestor2 = mydb.cursor()
    requestor2.execute("SELECT id FROM `unit_recording` WHERE unit_id="+unitId+" and record_date="+date)
    return requestor2.fetchall()[0]
run()