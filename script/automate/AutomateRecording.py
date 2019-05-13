from random import *

class AutomateRecording:
    automatId = 0
    automatType = 0x0000BA20
    tankTemperature = 8.0
    externalTemperature = 8.0
    milkTankWeight = 3512.0
    finalProductWeight = 0.0
    phMeasurement = 6.8
    kPosMeasurement = 35
    naClConcentration = 1.0
    salmonellaLevel = 17
    eColiLevel = 35
    listeriaLevel = 28

    def __init__(self, id):
        self.automatId += id
        self.automatType += random.uniform(0,16)
        self.tankTemperature += random.uniform(-5,5)
        self.externalTemperature += random.uniform(-5,5)
        self.milkTankWeight += random.uniform(-5,5)
        self.finalProductWeight += random.uniform(-5,5)
        self.phMeasurement += random.uniform(-5,5)
        self.kPosMeasurement += random.randint(-5,5)
        self.naClConcentration += random.uniform(-5,5)
        self.salmonellaLevel += random.randint(-5,5)
        self.eColiLevel += random.randint(-5,5)
        self.listeriaLevel += random.randint(-5,5)