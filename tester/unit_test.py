#! /usr/bin/env python2
'''
Created on Nov 3, 2014

@author: daineseh
'''
import unittest

class Function():
    def is_odd(self, num):
        if not isinstance(num, int):
            return False

        if not (num % 2):
            return False
        return True


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.__fun = Function()

    def test_case_1(self):
        result = self.__fun.is_odd('A')
        self.assertFalse(result, 'test_case_1')

    def test_case_2(self):
        result = self.__fun.is_odd(1)
        self.assertTrue(result, 'test_case_2')

    def test_case_3(self):
        expect = False
        result = self.__fun.is_odd('0')
        self.assertEqual(expect, result, 'test_case_2')

if __name__ == '__main__':
#     import sys; sys.argv = ['', 'TESTFunction.test_case_1']
    loader = unittest.defaultTestLoader.loadTestsFromTestCase(TestFunction)
    unittest.TextTestRunner().run(loader)
    unittest.main()