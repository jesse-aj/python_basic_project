"""
Name Mangling
"""



class BankAccount:
    def __init__(self, owner, balance=0 ):   #this gives the iternal value for the balance
        self.owner = owner
        self._balance = balance  # the underscore (_) shows that the balance can be used only internally not for outside use or manipulating


    def deposit(self, amount): #This a setter that allows to add to the balance buh not view the balance direct
        if amount  > 0: 
            self._balance += amount  # with this function the balance wont be shown only it just adds the deposited amount to the balance


    def get_balance(self):  #This is called and used as a getter so that balance will not be direct
        return self._balance
    

Jethro =  BankAccount("Jethro", 10000)
Jethro.deposit(100)
Wilberforce = BankAccount("", 200)
Wilberforce.get_balance()        


print(Jethro.get_balance())
