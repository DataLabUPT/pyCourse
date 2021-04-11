import unittest
from test_facultate import TestFacultate

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestFacultate('test_nume_facultate'))
    suite.addTest(TestFacultate('test_numar_studenti'))
    suite.addTest(TestFacultate('test_finantare'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
