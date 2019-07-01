import random
import json 

class AutomateRecording:
    automatId = 0
    automatType = 0x0
    tankTemperature = 0
    externalTemperature = 0
    milkTankWeight = 0
    finalProductWeight = 0.0
    phMeasurement = 0
    kPosMeasurement = 0
    naClConcentration = 0
    salmonellaLevel = 0
    eColiLevel = 0
    listeriaLevel = 0

    def __init__(self, id, haveError):
        self.automatId += id
        self.automatType = hex(47648 + random.randint(1,4))
        if haveError:
            print('Insert error')
            self.tankTemperature = random.uniform(100, 1000)
        else:
            self.tankTemperature = random.uniform(1, 75)
        self.externalTemperature = random.uniform(8,14)
        self.milkTankWeight = random.uniform(3512,4607)
        self.finalProductWeight = random.uniform(0,50)
        self.phMeasurement = random.uniform(6.8,7.2)
        self.kPosMeasurement = random.randint(35,47)
        self.naClConcentration = random.uniform(1,1.7)
        self.salmonellaLevel = random.randint(17,37)
        self.eColiLevel = random.randint(35,49)
        self.listeriaLevel = random.randint(28,54)

    def toJSON(self):
        return json.dumps(self.__dict__)