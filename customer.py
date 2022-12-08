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
        self.wallet_id_list = []


    def get_wallet(self, wallet_id):
        """Get a wallet by wallet id"""
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                return wallet
        return None

    def create_wallet(self, wallet_id, wallet_type):
        """Create a wallet for customer"""
        if wallet_type.title() == "Daily Use":
            wallet = DailyUseWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            sign = input("You have successfully create a daily use wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Saving":
            wallet = SavingWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            sign = input("You have successfully create a saving wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Holidays":
            wallet = HolidaysWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            sign = input("You have successfully create a holidays wallet, do you want to create another one?(y/n)")
        elif wallet_type.title() == "Mortgage":
            wallet = MortgageWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            sign = input("You have successfully create a mortgage wallet, do you want to create another one?(y/n)")
        else:
            sign = input("What kind of wallet do you want to create? Try again?(y/n)")
        return sign

    def delete_wallet(self, wallet_id):
        """Delete a wallet for customer"""
        count = 0
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                sign = input("This is your wallet and are you sure to delete it?(y/n)")
                if sign.lower() == 'y':
                    self.wallet_list.remove(wallet)
                    sign = input(f"You have successfully delete wallet({wallet_id}. Try again?(y/n)")
                    break
                else:
                    sign = input("Try again?(y/n)")
            count += 1
        if count == len(self.wallet_list):
            sign = input("This is not your wallet. Try again?(y/n)")
        return sign

    def deposit(self, wallet_id, amount):
        """Make a deposit for a customer"""
        count = 0
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                wallet.deposit(amount)
                sign = input("Transction succeeds. Do you want to deposit again?")
                break
            count += 1
        if count == len(self.wallet_list):
            sign = input("This is not your wallet. Try again?(y/n)")
        return sign
    
    def withdraw(self, wallet_id, amount):
        """Make a withdraw for a customer"""
        count = 0
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                judgment = wallet.withdraw(amount)
                if judgment.lower() == "s":
                    sign = input("Transcation succeeds. Do you want to withdraw again?(y/n)")
                elif judgment.lower() == "f":
                    sign = input("Transcation fails, this wallet have enough money, please try a small amount. Try again?(y/n)")
            count += 1
        if count == len(self.wallet_list):
            sign = input("Transcation fails, this is not your wallet. Try again?(y/n)")
        return sign
    
    def transfer_to_wallets(self, wallet_id_from, wallet_id_to, amount):
        """Transfer a customer's money from one wallet to another"""
        if wallet_id_from == wallet_id_to:
            sign = input("Transaction fails, you can't transfer money to the same wallet.Try again?(y/n)")
            transaction_fee = 0
        elif wallet_id_from not in self.wallet_id_list:
            sign = input("Transcation fails, you can just transfer from your wallets. Try again?(y/n)")
            transaction_fee = 0
        elif wallet_id_to not in self.wallet_id_list:
            sign = input("Transcation fails, you can just transfer to your wallets. Try again?(y/n)")
            transaction_fee = 0
        else:
            wallet = self.get_wallet(wallet_id_from)
            judgment, transaction_fee = wallet.transfer_to_wallets(wallet_id_to, amount)
            if judgment == "f":
                decision = input("Transaction fails, this wallet do not have enough money, find another to substitute?(y/n)")
                if decision == "y":
                    sign, transaction_fee = self.find_substitution_yourself(wallet_id_from, wallet_id_to, amount)
                else:
                    sign = input("Transaction fails, this wallet have enough money, please try a small amount. Try again?(y/n)")
            elif judgment == "s":
                sign = input("Transaction succeeds! Do you want to transfer to another wallet again(y/n)")
            elif judgment == "n":
                sign = input("Transaction fails, this wallet is not allowed to transfer to another one. Try again?(y/n)")
                        
        return sign, transaction_fee

    def transfer_to_others(self, wallet_id_from, customer, amount):
        """Transfer a customer's money to others"""
        if customer.wallet_list == []:
            sign = input("Transaction fails, this customer do not have any wallet. Try again?(y/n)")
            transaction_fee = 0
        if wallet_id_from not in self.wallet_id_list:
            sign = input("Transcation fails, you can just transfer from your wallets. Try again?(y/n)")
            transaction_fee = 0
        else:
            wallet = self.get_wallet(wallet_id_from)
            judgment, transaction_fee = wallet.transfer_to_other_customers(customer, amount)
            if judgment == "f":
                decision = input("Transaction fails, this wallet do not have enough money, find another to substitute?(y/n)")
                if decision == "y":
                    sign, transaction_fee = self.find_substitution_others(wallet_id_from, customer, amount)
                    sign = input("Transaction fails, this wallet have enough money, please try a small amount. Try again?(y/n)")
                elif judgment == "s":
                    sign = input("Transaction succeeds! Do you want to transfer to another wallet again(y/n)")
                elif judgment == "n":
                    sign = input("Transaction fails, this wallet is not allowed to transfer to another one. Try again?(y/n)")                 
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

    def find_substitution_yourself(self, wallet_id_from, wallet_id_to, amount):
        """When a customer's wallet does not have enough money, transfer from another wallet to own wallet"""
        wallet_list_copy = self.wallet_list.copy()
        wallet_list_copy.remove(self.get_wallet(wallet_id_from), self.get_wallet(wallet_id_to))
        count = 0
        for wallet in wallet_list_copy:
            if wallet.wallet_tpye in ["Daily Use","Holidays"]:#only daily use wallets and holidays wallets are allowed to transfer money to other wallets.
                judgment, transaction_fee = wallet.transfer_to_wallets(wallet_id_to, amount)
                if judgment == "f":
                    pass
                elif judgment == "s":
                    sign = input("Transaction succeeds! Do you want to transfer to another wallet again(y/n)")
                    break
            count += 1
        if count == len(wallet_list_copy):
            sign = input("Transaction fails, you don't have any qualified wallet. Try again?(y/n)")
            transaction_fee = 0
        return sign, transaction_fee

    def find_substitution_others(self, wallet_id_from, customer, amount):
        """When a customer's wallet does not have enough money, transfer from another wallet to another customer"""
        wallet_list_copy = self.wallet_list.copy()
        wallet_list_copy.remove(self.get_wallet(wallet_id_from))
        count = 0
        for wallet in wallet_list_copy:
            if wallet.wallet_tpye == "Daily Use":#only daily use wallets are allowed to transfer money to other customers.
                judgment, transaction_fee = wallet.transfer_to_other_customers(customer, amount)
                if judgment == "f":
                    pass
                elif judgment == "s":
                    sign = input("Transaction succeeds! Do you want to transfer to someone again(y/n)")
                    break
            count += 1
        if count == len(wallet_list_copy):
            sign = input("Transaction fails, you don't have any qualified wallet. Try again?(y/n)")
            transaction_fee = 0
        return sign, transaction_fee
