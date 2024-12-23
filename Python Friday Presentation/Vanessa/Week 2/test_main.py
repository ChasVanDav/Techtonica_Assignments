#testing functions (imported from main.py: add_numbers, multiply_numbers) using class (TestCalculations) importing unittest 'TestCase' method

import unittest
from main import add_numbers, multiply_numbers

class TestCalculations(unittest.TestCase):
            def test_add_numbers(self):
                #assertion on outcome for test case examples
                self.assertEqual(add_numbers(5, 3), 8) #expecting output = 8 & OK (success)
                self.assertEqual(add_numbers(-1, 1), 0) #expecting output = 0 & OK (success)
                #edge case of string input: 
                #self.assertEqual(add_numbers("three", 2), 5) 

            def test_multiply_numbers(self):
                #assertion on outcome for test case examples
                self.assertEqual(multiply_numbers(4, 5), 20) #expecting output = 20 & OK (success)
                self.assertEqual(multiply_numbers(-2, 3), -6) #expecting output = -6 & OK (success)
                
                #edge case of string input: 
                #self.assertEqual(multiply_numbers("apples", 2), 3) #expecting error message & failure

if __name__ == '__main__':
                 unittest.main()