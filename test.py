#! usr/bin/python

#import libraries
import unittest2
from vending import *


#create test class
class TDDVendingMachine(unittest2.TestCase):
       
       #create vending machine object   
       def setUp(self):
            self.vm=vendingMachine()
 
       #test accept nickel
       def test_1_insert_nickel_returns_correct_result(self):
             nickel=self.vm.insert()
             self.assertEqual(0.05,nickel)
       
       #test accept dime  
       def test_2_insert_dime_returns_correct_result(self):
             dime=self.vm.insert()
             self.assertEqual(0.10,dime)

       #test accept quarter
       def test_3_insert_quarter_returns_correct_result(self):
             quarter=self.vm.insert()
             self.assertEqual(0.25,quarter)
       
       #test return invalid coins
       def test_4_return_invalid_coins(self):
             invalid=self.vm.insert()
             self.assertEqual('abc',invalid)

       #test select any item and pay the exact price
       def test_5_select_product(self):
             product=self.vm.SELECT()
             self.assertEqual('THANK YOU!',product)

       #test return change $0.15 
       def test_6_make_change(self):
             make_change=self.vm.send_to_return(0.15)
             self.assertEqual('dn',make_change)

       #test return change $0.40
       def test_7_make_change(self):
             make_change=self.vm.send_to_return(0.40)
             self.assertEqual('qdn',make_change)
       
       #test return change $0.85
       def test_8_make_change(self):
             make_change=self.vm.send_to_return(0.85)
             self.assertEqual('qqqd',make_change)

       #test return inserted coins(sequence n,d,q,a,b,c) after cancellation of a purchase
       def test_9_return_all_coins_to_cancel_a_purchase(self):
             all_coins=self.vm.SELECT()
             self.assertEqual('abcndq',all_coins)
       
       #test item is available
       def test_10_check_avilable(self):
             self.vm1=vendingMachine(1)
             available=self.vm1.sold_out('cola')
             self.assertEqual('Available',available)

       #test item is sold out
       def test_11_check_sold_out(self):
             self.vm2=vendingMachine(0)
             sold=self.vm2.sold_out('cola')
             self.assertEqual('SOLD OUT',sold)

       
    
         
#driver function
if __name__=='__main__':
       unittest2.main()
