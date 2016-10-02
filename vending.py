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
            else:
                self.name='Invalid coin'
                self.value=0
            
                

           
#vending machine calass
class vendingMachine():

      #insert coins
      def insert(self):
              inp=raw_input("Insert coin(n for 'Nickel', d for 'Dime', q for 'Quarter'):")
              coin=coins(inp)
              if coin.value==0:
                     print 'Invalid coin, please insert Nickels, Dimes or Quarters'
                     coin.value+=self.insert()
              return coin.value
              
               
