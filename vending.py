#! usr/bin/python

#create coins
class coins():
       
      def __init__(self,symbol):
            self.name=None
            self.coinsValue(symbol)

      def coinsValue(self,k):
            if k=='n':
                self.name='nickel'
                self.value=5
            elif k=='d':
                self.name='dime'
                self.value=10
            elif k=='q':
                self.name='quarter'
                self.value=25
            return
            
                

           
#vending machine calass
class vendingMachine():

      #insert coins
      def insert(self):
              inp=raw_input('Insert coin:')
              coin=coins(inp)
              return coin.value
              
               
