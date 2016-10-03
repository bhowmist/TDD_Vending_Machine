#! usr/bin/python

from decimal import Decimal

#create coins
class coins():
       
      def __init__(self,symbol):
            self.name=None
            self.coinsValue(symbol)

      def coinsValue(self,k):
            if k=='n':
                self.name='nickel'
                self.value=0.05
            elif k=='d':
                self.name='dime'
                self.value=0.10
            elif k=='q':
                self.name='quarter'
                self.value=0.25
            else:
                self.name='Invalid coin'
                self.value=0.00
            
                

           
#vending machine calass
class vendingMachine():

      def __init__(self):
             self.invalid=''
             self.accepted=''
             

      #insert coins
      def insert(self):
              inp=''
              coin=coins(inp)
              while coin.value==0:
                      self.invalid+=inp
                      inp=raw_input("Insert coin or press r to return:")
                      if inp =='r':
                            return self.Return()
                      coin=coins(inp)
                      #if invalid coin, display message 
                      if coin.value==0:
                          print 'Insert a valid coin(n,d,q)!' 
              self.accepted+=inp
              return coin.value
                  
                  

      #return coins
      def Return(self):
           if self.invalid!=None or self.accepted!=None:
                  s=self.invalid+self.accepted
                  self.invalid=''
                  self.accepted=''
                  return s
           else:
                 return 'Nothing to return'


      #select product
      def SELECT(self):
           #avilable products
           products={'cola':1.00,'chips':0.50,'candy':0.65}
           #choose an item
           item=raw_input('Select an item, cola, chips or candy: ')
           print 'You have selected '+item +', ', 
           #price to be paid
           remaining_price=(products[item])
           #accept coins and update display
           while remaining_price>0.0:
                   print 'Price : $'+ str(remaining_price)
                   inserted=(self.insert())
                   remaining_price=(round(Decimal(remaining_price),2)-round(Decimal(inserted),2))
           #take care of the change
           if remaining_price<0.0:
                   self.accepted=''
                   send_to_return(abs(remaining_price))
           #success message
           print 'THANK YOU!'
           return 'THANK YOU!'

    
      #Make change
      def send_to_return(self,change):
           change=int(change*100)
           while change>0.0:
                if change>=25:
                      self.invalid+='q'
                      val=25
                if ((change>=10) and (change<25)):
                      self.invalid+='d'
                      val=10
                if ((change>=5) and (change<10)):
                      self.invalid+='n'
                      val=5
                change=(change-val)
           S= self.Return()
           print S
           return S
                 
             
                     
        
              
               
