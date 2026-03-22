import json
import random as rd

class accounts:
    def __init__(self,name,password,id=None,balance=0,activation=True):
        self.name = name
        self.password = password
        self.id = id
        self.balance = balance
        self.activation = activation
        self.data = {}

    def vertify(self):
       if self.id not in self.data.keys():
          print("Id doesn't exist")
          return False
       if self.password != self.data[self.id]['password']:
          print('Password is incorrect')
          return False
       if not self.data[self.id]['activation']:
        print('Account is deactivated!')
        return False
       return True

    def vertify2(self):
       if self.id not in self.data.keys():
          print("Id doesn't exist")
          return False
       if self.password != self.data[self.id]['password']:
          print('Password is incorrect')
          return False
       return True

    def save(self):
        with open('accounts.json','w') as f:
            json.dump(self.data,f,indent=4)

    def load(self):
        try:
            with open('accounts.json','r') as f:
                self.data = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            self.data = {}
            self.save()

    def create(self):
        self.load()
        self.id = ''.join([str(rd.randint(0,9)) for i in range(12)])
        while self.id in self.data.keys():
         self.id = ''.join([str(rd.randint(0,9)) for i in range(12)])
        self.data[self.id] = {'name':self.name,'password':self.password,'balance':self.balance,'activation':self.activation}
        self.save()
        print('Account Is Created Successfully')

    def add(self):
        self.load()
        if self.vertify():
         self.data[self.id]['balance'] += self.balance 
         print('Account Is Added Successfully') 
         self.save()
      
    def withdraw(self):
        self.load()
        if self.vertify():
         if self.balance <= self.data[self.id]['balance']:
          self.data[self.id]['balance'] -= self.balance  
          print('Account Is Withdrawed Successfully')
          self.save()
         else:
           print('No Enough Money In The Bank Acccount')
    
    def activate(self):
        self.load()
        if self.vertify2():
         if self.data[self.id]['activation'] == True:
            print('It is already activated')
         else:
            self.data[self.id]['activation'] = True
            self.save()
            print('account is activated')

    def deactivate(self):
       self.load()
       if self.vertify2():
        if self.data[self.id]['activation'] == False:
            print('It is already deactivated')
        else:
         self.data[self.id]['activation'] = False
         self.save()
         print('account is deactivated')
    
    def transfer(self,new_id):
        self.load()
        if self.vertify():
         if new_id != self.id:
          if new_id not in self.data.keys():
           print("Id doesn't exist")
           return False
          else:
           if self.balance <= self.data[self.id]['balance']:
            self.data[self.id]['balance'] -= self.balance  
            self.data[new_id]['balance'] += self.balance 
            self.save()
            print('Money Is Transferred Successfully')
           else:
            print('Not Enough Money In The Bank Account')
         else:
            print('Both are the same Ids')
    
    def delete(self):
       self.load()
       if self.vertify():
          del self.data[self.id]
          self.save()
          print('Account Is Deleted Successfully')

    def Balance(self):
       self.load()
       if self.vertify2():
        print(f"Welcome {self.data[self.id]['name']}\n Balance: ${self.data[self.id]['balance']}")