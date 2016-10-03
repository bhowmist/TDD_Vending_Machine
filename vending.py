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
            
                     
        
              
               
