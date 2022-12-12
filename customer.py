from wallet import *
# from banking_system import *

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
            print("You have successfully create a daily use wallet, going back...")
        elif wallet_type.title() == "Saving":
            wallet = SavingWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            print("You have successfully create a saving wallet, going back...")
        elif wallet_type.title() == "Holidays":
            wallet = HolidaysWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            print("You have successfully create a holidays wallet, going back...")
        elif wallet_type.title() == "Mortgage":
            wallet = MortgageWallet(wallet_id)
            self.wallet_list.append(wallet)
            self.wallet_id_list.append(wallet_id)
            print("You have successfully create a mortgage wallet, going back...")

    def delete_wallet(self, wallet_id):
        """Delete a wallet for customer"""
        if len(self.wallet_list) == 0:
            print("You have to create a wallet first. Going back...")
        else:
            count = 0
            wallet_id_list_copy = self.wallet_id_list.copy()
            for wallet in self.wallet_list:
                if wallet.wallet_id == wallet_id:
                    sign = input("This is your wallet and are you sure to delete it?(y/n)")
                    if sign.lower() == 'y':
                        self.wallet_list.remove(wallet)
                        self.wallet_id_list.remove(wallet_id)
                        print(f"You have successfully delete wallet({wallet_id}). Going back...")
                        break
                    else:
                        print(f"You don't delete wallet({wallet_id}). Going back...")
                        break
                count += 1
            if count == len(wallet_id_list_copy):
                print("You don't have this wallet. Going back..")
               
    def deposit(self, wallet_id, amount):
        """Make a deposit for a customer"""
        count = 0
        amount = float(amount)
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                wallet.deposit(amount)
                print("Transction succeeds. Going back...")
                break
            count += 1
        if count == len(self.wallet_list):
            print("You don't have this wallet. Going back...")
              
    def withdraw(self, wallet_id, amount):
        """Make a withdraw for a customer"""     
        count = 0
        amount = float(amount)
        for wallet in self.wallet_list:
            if wallet.wallet_id == wallet_id:
                judgment = wallet.withdraw(amount)
                if judgment.lower() == "s":
                    print("Transcation succeeds. Going back...")
                    break
                elif judgment.lower() == "f":
                    print("Transcation fails, this wallet have enough money, please try a small amount. Going back...")
                    break
                elif judgment.lower() == "n":
                    print("Transcation fails, this wallet does not have the attribute to withdraw. Going back...")
                    break
            count += 1
        if count == len(self.wallet_list):
            print("Transcation fails, this is not your wallet. Going back...")
    
    def transfer_to_wallets(self, wallet_id_from, wallet_id_to, amount):
        """Transfer a customer's money from one wallet to another"""
        amount = float(amount)
        wallet_to = self.get_wallet(wallet_id_to)
        if wallet_id_from == wallet_id_to:
            print("Transaction fails, you can't transfer money to the same wallet. Going back...")
            transaction_fee = 0
        elif wallet_id_from not in self.wallet_id_list:
            print("Transcation fails, you can just transfer from your wallets. Going back...")
            transaction_fee = 0
        elif wallet_id_to not in self.wallet_id_list:
            print("Transcation fails, you can just transfer to your wallets.  Going back...")
            transaction_fee = 0
        else:
            wallet_from = self.get_wallet(wallet_id_from)
            judgment, transaction_fee = wallet_from.transfer_to_wallets(wallet_to, amount)
            if judgment == "f":
                decision = input("Transaction fails, this wallet do not have enough money, find another to substitute?(y/n)")
                if decision == "y":
                   transaction_fee = self.find_substitution_yourself(wallet_id_from, wallet_to, amount)
                else:
                    print("Transaction fails, this wallet don't have enough money, please try a small amount.  Going back...")
            elif judgment == "s":
                print("Transaction succeeds!  Going back...")
            elif judgment == "n":
                print("Transaction fails, this wallet is not allowed to transfer to another one.  Going back...")
                        
        return transaction_fee

    def transfer_to_others(self, wallet_id_from, customer, amount):
        amount = float(amount)
        """Transfer a customer's money to others"""
        if customer.wallet_list == []:
            print("Transaction fails, this customer do not have any wallet.  Going back...")
            transaction_fee = 0
        elif wallet_id_from not in self.wallet_id_list:
            print("Transcation fails, you can just transfer from your wallets.  Going back...")
            transaction_fee = 0
        else:
            wallet = self.get_wallet(wallet_id_from)
            judgment, transaction_fee = wallet.transfer_to_other_customers(customer, amount)
            if judgment == "f":
                decision = input("Transaction fails, this wallet do not have enough money, find another to substitute?(y/n)")
                if decision == "y":
                    transaction_fee = self.find_substitution_others(wallet_id_from, customer, amount)
                else:
                    print("Transaction fails, this wallet have enough money, please try a small amount.  Going back...")
            elif judgment == "s":
                    print("Transaction succeeds!  Going back...")
            elif judgment == "n":
                    print("Transaction fails, this wallet is not allowed to transfer to another one.  Going back...")                 
        return transaction_fee
    
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

    def find_substitution_yourself(self, wallet_id_from, wallet_to, amount):
        """When a customer's wallet does not have enough money, transfer from another wallet to own wallet"""
        amount = float(amount)
        wallet_list_copy = self.wallet_list.copy()
        wallet_list_copy.remove(self.get_wallet(wallet_id_from))
        wallet_list_copy.remove(wallet_to)
        count = 0
        for wallet in wallet_list_copy:
            if wallet.wallet_type in ["Daily Use","Holidays"]:#only daily use wallets and holidays wallets are allowed to transfer money to other wallets.
                judgment, transaction_fee = wallet.transfer_to_wallets(wallet_to, amount)
                if judgment == "f":
                    print("Transaction fails, your other wallets don't have enough money. Going back...")
                    break
                elif judgment == "s":
                    print("Transaction succeeds!  Going back...")
                    break
            count += 1
        if count == len(wallet_list_copy):
            print("Transaction fails, you don't have any qualified wallet.  Going back...")
            transaction_fee = 0
        return transaction_fee

    def find_substitution_others(self, wallet_id_from, customer, amount):
        """When a customer's wallet does not have enough money, transfer from another wallet to another customer"""
        amount = float(amount)
        wallet_list_copy = self.wallet_list.copy()
        wallet_list_copy.remove(self.get_wallet(wallet_id_from))
        count = 0
        for wallet in wallet_list_copy:
            if wallet.wallet_type == "Daily Use":#only daily use wallets are allowed to transfer money to other customers.
                judgment, transaction_fee = wallet.transfer_to_other_customers(customer, amount)
                if judgment == "f":
                    print("Transaction fails, your other wallets don't have enough money, please try a small amount.  Going back...")
                    break
                elif judgment == "s":
                    print("Transaction succeeds!  Going back...")
                    break
            count += 1
        if count == len(wallet_list_copy):
            print("Transaction fails, you don't have any qualified wallet.  Going back...")
            transaction_fee = 0
        return transaction_fee
    
    def change_password(self, old_password, new_password):
        """Change the password of a customer"""
        if old_password == self.password:
            self.password = new_password
            print("Password changed successfully!")
        else:
            print("Your old password is wrong, please try again.")