from wallet import *


class Customer:

    def __init__(self, first_name, last_name, country_of_residence, age, email, password, user_name):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.country_of_residence = country_of_residence
        self.age = age
        self.email = email
        self.password = password
        self.user_name = user_name#user name is unique for each customer
        self.wallet_list = []
        self.full_name = f"{self.first_name} {self.last_name}"

    def create_wallet(self, wallet_id, wallet_type):
        """Create a wallet for customer"""
        if wallet_type.title() == "Daily Use":
            wallet = DailyUseWallet(wallet_id)
            self.wallet_list.append(wallet)
            sign = input("You have successfully create a daily use wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Saving":
            wallet = SavingWallet(wallet_id)
            self.wallet_list.append(wallet)
            sign = input("You have successfully create a saving wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Holidays":
            wallet = HolidaysWallet(wallet_id)
            self.wallet_list.append(wallet)
            sign = input("You have successfully create a holidays wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Mortgage":
            wallet = MortgageWallet(wallet_id)
            self.wallet_list.append(wallet)
            sign = input("You have successfully create a mortgage wallet, do you want to create another one?(y/n)")
        else:
            sign = input("What kind of wallet do you want to create? Try again?(y/n)")
        return sign

    def delete_wallet(self, wallet_id):
        """Delete a wallet for customer"""
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                sign = input("This is your wallet and are you sure to delete it?(y/n)")
                if sign.lower() == 'y':
                    self.wallet_list.remove(wallet)
                    print(f"You have successfully delete wallet({wallet_id})")
                    break
                else:
                    sign = input("Try again?(y/n)")
            else:
                sign = input("This is not your wallet. Try again?(y/n)")
        return sign

    def deposit(self, wallet_id, amount):
        """Make a deposit for a customer"""
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                wallet.deposit(amount)
                sign = input("Transction succeeds. Do you want to deposit again?")
                break
            else:
                sign = input("Transction fails, this is not your wallet. Try again?(y/n)")
        return sign
    
    def withdraw(self, wallet_id, amount):
        """Make a withdraw for a customer"""
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                judgment = wallet.withdraw(amount)
                if judgment.lower() == "s":
                    sign = input("Transcation succeeds. Do you want to withdraw again?")
            else:
                sign = input("Transcation fails, this is not your wallet. Try again?(y/n)")
        return sign
    
    def transfer_to_wallets(self, wallet_id_from, wallet_id_to, amount):
        """Transfer a customer's money from one wallet to another"""
        if wallet_id_from == wallet_id_to:
            sign = input("Transaction fails, you can't transfer money to the same wallet.Try again?(y/n)")
            transaction_fee = 0
        else:
            for wallet in self.wallet_list:
                if wallet.wallet_id == wallet_id_from:
                    for wallet in self.wallet_list:
                        if wallet.wallet_id == wallet_id_to:
                            judgment, transaction_fee = wallet.transfer_to_wallets(wallet_id_to, amount)
                            if judgment == "f":
                                sign = input("Transaction fails, you don't have enough money, please try a small amount. Try again?(y/n)")
                            elif judgment == "s":
                                sign = input("Transaction succeeds! Do you want to transfer to another wallet again(y/n)")
                            elif judgment == "n":
                                sign = input("Transaction fails, this wallet is not allowed to transfer to another one. Try again?(y/n)")
                        else:
                            sign = input("Transaction fails, you can not transfer money to other's wallet. Try again?(y/n)")
                            transaction_fee = 0
                else:
                    sign = input("Transcation fails. Please check if this is your wallet. Try again?(y/n)")
                    transaction_fee = 0
        return sign, transaction_fee

    def transfer_to_others(self, wallet_id_from, customer, amount):
        """Transfer a customer's money to others"""
        if customer.wallet_list == []:
            sign = input("Transaction fails, this customer doesn't have any wallet. Try again?(y/n)")
            transaction_fee = 0
        else:
            for wallet in self.wallet_list:
                if wallet.wallet_id == wallet_id_from:
                    judgment, transaction_fee = wallet.transfer_to_wallet(customer, amount)
                    if judgment == "f":
                        sign = input("Transaction fails, you don't have enough money, please try a small amount. Try again?(y/n)")
                    elif judgment == "s":
                        sign = input("Transaction succeeds! Do you want to transfer to someone again(y/n)")
                    elif judgment == "n":
                        sign = input("Transaction fails, this wallet is not allowed to transfer to another customer. Try again?(y/n)")
                else:
                    sign = input("Transcation fails. Please check if this is your wallet. Try again?(y/n)")
                    transaction_fee = 0
        return sign, transaction_fee
    
    def check_my_wallets(self):
        """Check all the wallets of a customer"""
        if self.wallet_list == []:
            print("You don't have any wallet.")
        else:
            for wallet in self.wallet_list:
                print(f"Wallet ID: {wallet.wallet_id}")
                print(f"Wallet Type: {wallet.wallet_type}")
                print(f"Balance: {wallet.balance}")
                print(f"Last transaction: {wallet.last_transaction}")
                print("")   