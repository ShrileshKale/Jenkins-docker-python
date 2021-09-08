import time,sys
import unittest

def hello():
    return "Hello World"

def sum_two_number(x=2,y=5):
    return x+y

def sub_two_number(x=2,y=5):
    return x-y

class TestCalc(unittest.TestCase):

    def test_sum_two_number(self):
        result = sum_two_number(2,3)
        self.assertEqual(result, 5)

    
    def test_sub_two_number(self):
        result = sub_two_number(3,3)
        self.assertEqual(result, 0)

    def test_hello(self):
        result = hello()
        self.assertEqual(result, 'Hello World')



if __name__ == '__main__':
    unittest.main()