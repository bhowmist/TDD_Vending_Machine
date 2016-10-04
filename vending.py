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

      def __init__(self,quantity=10):
             self.invalid=''
             self.accepted=''
             #avilable products
             self.products={'cola':[1.00,quantity],'chips':[0.50,quantity],'candy':[0.65,quantity]} 
             

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
                  print 'please collect your coins!'
                  print s
                  return s
           else:
                 return 'No coins to return!'


      #select product
      def SELECT(self):
           #choose an item
           item=raw_input('Select an item, cola, chips or candy: ')
           #check if the item is available
           if self.sold_out(item)=='SOLD OUT':
                     print 'SOLD OUT'
                     return 'SOLD OUT'
           else:
                     pass 
           print 'You have selected '+item +', ', 
           #price to be paid
           remaining_price=(self.products[item][0])
           #accept coins and update display
           while remaining_price>0.0:
                   print 'Price : $'+ str(remaining_price)
                   inserted=(self.insert())
                   try:
                       remaining_price=(round(Decimal(remaining_price),2)-round(Decimal(inserted),2))
                   except:
                       #return coins
                       return inserted
           #take care of the change
           self.accepted=''
           if remaining_price<0.0:
                   self.send_to_return(abs(remaining_price))
           #quantity of the item is decreased by 1
           self.sold(item)
           #success message
           print 'THANK YOU!'
           return 'THANK YOU!'


      #one item sold
      def sold(self,item):
           self.products[item][1]-=1
           return
          

    
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
           return S


      #sold out
      def sold_out(self,item):
             if self.products[item][1]==0:
                      return 'SOLD OUT'
             return 'Available'    
                 
             
                     
        
              
               
