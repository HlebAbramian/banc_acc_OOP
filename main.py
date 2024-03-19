#**Задание: Создание класса "Банковский счет"**

#1. Создайте класс BankAccount, который будет представлять банковский
# счет с атрибутами account_number (номер счета), balance (баланс) и owner (владелец счета).

#2. Добавьте метод __init__, который будет инициализировать атрибуты
# account_number, balance и owner при создании объекта.

#3. Добавьте методы для пополнения (deposit) и снятия (withdraw) средств со счета.

#4. Реализуйте метод display_account_info, который будет выводить информацию о банковском счете 
# в формате: "Счет №{account_number}, Владелец: {owner}, Баланс: {balance}".

#5. Добавьте возможность перевода средств между двумя банковскими счетами (метод transfer).


class BankAccount: 
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawal(self, amount):
        
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Not enough funds on account')
            
    def display_account_info (self):
        print(f'Account №{self.account_number}, Owner: {self.owner}, Balance: {self.balance}')
        
        
    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            print(f'trahsfer{amount} made succes.')
        else:
            print("Not enough funs on account for transfer.")
        
             
print('*' * 40)            
account1 = BankAccount("12", 1000, "John")
account2 = BankAccount("54", 500, "Anastasia")
account1.display_account_info()
account2.display_account_info()
print('*' * 40)
account1.deposit(500)
account2.withdrawal(200)
account1.transfer(account2, 300)
print('*' * 40)
account1.display_account_info()
account2.display_account_info()
print('*' * 40) 