'''
Created on Jan 17, 2017

@author: Liming
'''
import unittest
from src.Question import Section_Collector

class Test(unittest.TestCase):

    def setUp(self):
        self.q = Section_Collector("question_test.txt")

    def test_read_from_file(self):
        self.assertEqual(self.q.section.name, "CATEGORY", "header failed")
        
        self.assertEqual(len(self.q.section.subsections), 3, "subsection count error")
        
        self.assertEqual(self.q.section.subsections[0].data_type, "alpha", "read input failed")
        self.assertEqual(self.q.section.subsections[1].data_type, "beta", "read input failed")
        self.assertEqual(self.q.section.subsections[2].data_type, "gamma", "read input failed")

    def test_read_user_input(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()