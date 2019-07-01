import unittest
import json
from dbStorage import checkOutLimit, checkData

class TestStringMethods(unittest.TestCase):

    def test_checkOutLimit(self):
        self.assertEqual(checkOutLimit(5,1,10), False)
        self.assertEqual(checkOutLimit(1,5,10), True)
        self.assertEqual(checkOutLimit(15,5,10), True)
    def test_checkData(self):
        data = json.loads('{"automatId": 3, "automatType": "0xba23", "tankTemperature": 26.17972768290544, "externalTemperature": 10.69894218971626, "milkTankWeight": 4346.429420888058, "finalProductWeight": 39.76007479401552, "phMeasurement": 6.963457948279842, "kPosMeasurement": 40, "naClConcentration": 1.1728133145453221, "salmonellaLevel": 29, "eColiLevel": 35, "listeriaLevel": 37}')
        self.assertEqual(checkData(data,1), True)

if __name__ == "__main__":
    unittest.main()