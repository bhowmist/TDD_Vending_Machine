#! usr/bin/python

#import libraries
import unittest2
from vending import *


#create test class
class TDDVendingMachine(unittest2.TestCase):
          
       def setUp(self):
            self.vm=vendingMachine()

       def test_1_insert_nickel_returns_correct_result(self):
             nickel=self.vm.insert()
             self.assertEqual(5,nickel)
      
       def test_2_insert_dime_returns_correct_result(self):
             dime=self.vm.insert()
             self.assertEqual(10,dime)

       def test_3_insert_quarter_returns_correct_result(self):
             quarter=self.vm.insert()
             self.assertEqual(25,quarter)

            
      
       

#driver function
if __name__=='__main__':
       unittest2.main()
