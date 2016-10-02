#! usr/bin/python

#import libraries
import unittest2
from vending import *


#create test class
class TDDVendingMachine(unittest2.TestCase):
       
       def test_insert_nickel_returns_correct_result(self):
             vm=vendingMachine()
             coin=vm.insert()
             self.assertEqual(10,coin)

#driver function
if __name__=='__main__':
       unittest2.main()
