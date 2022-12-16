# -*- coding: utf-8 -*-
"""
Created on Tues Dec 13 16:21:00 2022

This is the wallet class, which is used to create a wallet object, and the wallet object contains the following functions:
1.deposit: which is used to deposit money.
2.withdraw: which is used to withdraw money.
3.transfer to wallets: which is used to transfer money to other wallets of the same customer.
4.transfer to other_customers: which is used to transfer money to other customers.

Wallets are created by the customer class, and the customer class will create wallet objects for each customer.
All functions are written in the wallet class, and then create 4 subclasses to inherit all the methods and variables of the parent class.
When the wallet corresponding to the subclass has no function, rewrite the method of the parent class to achieve functional control。
@ author: Jinyu Meng(sw22365@bristol.ac.uk)
"""

class Wallet:

    def __init__(self, wallet_id):
        """Initialization"""
        self.wallet_id = wallet_id
        self.balance = 0
        self.last_transaction = "None"
        
    def deposit(self, amount):
        """Make a deposit"""
        self.balance += amount
        self.last_transaction = f"Deposit {amount}"

    def withdraw(self, amount):
        """free withdraw"""
        if amount >= self.balance:
            sign = "f"#f for fail
        else:
            self.balance -= amount
            self.last_transaction = f"Withdraw {amount}"
            sign = "s"#s for success
        return sign

    def transfer_to_wallets(self, wallet_to, amount):
        """Transfer among wallets, 0.5% fee"""
        if amount * 1.005  > self.balance:
            sign = "f"#f for fail
            fee = 0
        else:
            self.balance -= amount * 1.005 #0.5% fee
            wallet_to.balance += amount
            fee = amount * 0.005
            self.last_transaction = f"Transfer {amount} to wallet({wallet_to.wallet_id})"
            sign = "s"#s for success
        return sign, fee#fee will go to the system account

    def transfer_to_other_customers(self, customer, amount):
        """Transfer to others, 1.5% fee, the receiving wallet is arranged according to the number of its' functions"""
        if amount * 1.015 > self.balance:
            sign = "f"#f for fail
            fee = 0
        else:
            for wallet in customer.wallet_list:
                if wallet.wallet_type == "Daily Use":#4 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                    break
                elif wallet.wallet_type == "Holidays":#3 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                    break
                elif wallet.wallet_type == "Saving":#2 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                    break
                elif wallet.wallet_type == "Mortgage":#1 function
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                    break
        return sign, fee#fee will go to the system account
     
       
class DailyUseWallet(Wallet):
    """The unique feature of a daily use wallet"""
    def __init__(self, wallet_id):
        """Initialize parent class attributes"""
        super().__init__(wallet_id)
        self.wallet_type = "Daily Use"


class SavingWallet(Wallet):
    """The unique feature of a saving wallet"""
    def __init__(self, wallet_id):
        """"Initialize parent class attributes"""
        super().__init__(wallet_id)
        self.wallet_type = "Saving"

    def transfer_to_wallets(self, wallet_to, amount):
        """Saving wallets are not allowed to transfer to other wallet"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee

    def transfer_to_other_customers(self, customer, amount):
        """Saving wallets are not allowed to transfer to other customer"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee


class HolidaysWallet(Wallet):
    """The unique feature of a holidays wallet"""
    def __init__(self, wallet_id):
        """Initialize parent class attributes"""
        super().__init__(wallet_id)
        self.wallet_type = "Holidays"

    def transfer_to_other_customers(self, customer, amount):
        """Holidays wallets are not allowed to transfer to other customer"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee


class MortgageWallet(Wallet):
    """The unique feature of a mortgage wallet"""
    def __init__(self, wallet_id):
        """"Initialize parent class attributes"""
        super().__init__(wallet_id)
        self.wallet_type = "Mortgage"

    def withdraw(self, amount):
        """Mortgage wallets are not allowed to withdraw"""
        sign = "n"#n for not allowed
        return sign

    def transfer_to_wallets(self, wallet_to, amount):
        """Mortgage wallets are not allowed to transfer to other wallet"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee

    def transfer_to_other_customers(self, customer, amount):
        """Mortgage wallets are not allowed to transfer to other customer"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee