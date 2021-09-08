# test_code1.py

import unittest
import code1 # the other file

class TestCap(unittest.TestCase): # inheriting from the unittest.TestCase
    
    def test_one_word(self):
        text = 'python'
        result = code1.cap_text(text) # the function from the code1 file
        self.assertEqual(result,'Python')

    def test_multible_words(self):
        text = 'monty python'
        result = code1.cap_text(text)
        self.assertEqual(result,'Monty Python') # this will fail cause it should be 'Monty python'

if __name__ == "__main__":
    unittest.main()