import unittest
from dbStorage import checkOutLimit

class TestStringMethods(unittest.TestCase):

    def test_checkOutLimit(self):
        self.assertEqual(checkOutLimit(5,1,10), True)
        self.assertEqual(checkOutLimit(1,5,10), False)
        self.assertEqual(checkOutLimit(15,5,10), False)

if __name__ == '__main__':
    unittest.main()