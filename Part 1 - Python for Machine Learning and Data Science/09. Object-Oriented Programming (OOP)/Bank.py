# accessing some part of data 
class Bank:
    def __init__(self):
        self.accno = 10013044290015
        self.name = 'Shri Devi'
        self.balance = 5000000.00
        self.__loan = 150000.00
    
    def display_to_clerk(self):
        print('Account no:', self.accno)
        print('Name:', self.name)        
        print(f'Balance: {self.balance:.2f}')
    
# Object creation must be outside the class
m = Bank()
m.display_to_clerk()