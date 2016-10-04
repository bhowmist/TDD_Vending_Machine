#! usr/bin/python

'''n=nickel,d=dime,q=quarter,p=penny'''

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
             self.coin_change=''

             #avilable products
             self.products={'cola':[1.00,quantity],'chips':[0.50,quantity],'candy':[0.65,quantity]} 

             #minimum # of each coin to avoid exact change(can be any #,here set as 2)
             self.num={'n':2,'d':2,'q':2}
             
             

      #Insert coins
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

              #update coin numbers
              self.accepted+=inp
              self.num[inp]+=1
              return coin.value
                  
                  

      #Return coins
      def Return(self):
           s=''
           if self.invalid!='' or self.accepted!='' or self.coin_change!='':
                  s=self.invalid+self.accepted+self.coin_change
                  if self.accepted!='':
                     for i in self.accepted:
                               self.num[i]-=1
                  self.invalid=''
                  self.accepted=''
                  self.coin_change=''
           if s!='':
                  print '\nPlease collect your coins!'
                  print s+'\n'
                  return s
           else:
                 print '\nNo coins to return!\n'
                 return 'No coins to return!'


      #Select product
      def SELECT(self):
           self.exact()
           item=''
           #choose an item
           while item=='':
                 item=raw_input('Select an item, cola, chips or candy: ')
                 if item!='cola' and item!='chips' and item!='candy':
                             print '**Select a valid item!**'
                             item=''
           #check if the item is available
           if self.sold_out(item)=='SOLD OUT':
                     print '**SOLD OUT**'
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
           self.sold(item)
           if remaining_price<0.0:
                    self.send_to_return(abs(remaining_price))    
           else:
                 self.accepted=''
                 self.Return()
                      
           #success message
           print '\n**THANK YOU!!**\n'
           return 'THANK YOU!'
           


      #One item sold
      def sold(self,item):
           self.products[item][1]-=1
           return
          

    
      #Make change
      def send_to_return(self,change):
           change=int(change*100)
           while change>0.0:
                if change>=25:
                      self.coin_change+='q'
                      val=25
                if ((change>=10) and (change<25)):
                      self.coin_change+='d'
                      val=10
                if ((change>=5) and (change<10)):
                      self.coin_change+='n'
                      val=5
                change=(change-val)
           for i in self.coin_change:
                  self.num[i]-=1
           S= self.Return()
           return S


      #Sold out
      def sold_out(self,item):
             if self.products[item][1]==0:
                      return 'SOLD OUT'
             return 'Available' 

      #Exact change
      def exact(self):
             for i in self.num.values():
                    if i<2:
                        print '------------------'
                        print 'EXACT CHANGE ONLY!'
                        print '------------------'
                        print '\n'
                        return 'EXACT'
                    else:
                         pass 

                     
             
'''#Driver function
if __name__=='__main__':
         v=vendingMachine()
         while True:
              v.SELECT()'''
                            
        
              
               
