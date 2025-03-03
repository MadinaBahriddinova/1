import json
import random

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"
    
    def __repr__(self):
        return f"Account({self.account_number}, {self.name}, {self.balance})"

class Bank:
    FILE_NAME = "accounts.json"
    
    def __init__(self):
        self.accounts = self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(1000, 9999))
        while account_number in self.accounts:
            account_number = str(random.randint(1000, 9999))
        self.accounts[account_number] = Account(account_number, name, initial_deposit).__dict__
        self.save_to_file()
        return f"Account created! Account Number: {account_number}"
    
    def view_account(self, account_number):
        return self.accounts.get(account_number, "Account not found")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            acc["balance"] += amount
            self.save_to_file()
            return f"Deposited {amount}. New balance: {acc['balance']}"
        return "Account not found"
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            if amount > acc["balance"]:
                return "Insufficient funds"
            acc["balance"] -= amount
            self.save_to_file()
            return f"Withdrew {amount}. New balance: {acc['balance']}"
        return "Account not found"
    
    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.accounts, file, indent=4)
    
    def load_from_file(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

# Example Usage
bank = Bank()
print(bank.create_account("Alice", 500))
print(bank.deposit("1001", 200))
print(bank.withdraw("1001", 100))
print(bank.view_account("1001"))
