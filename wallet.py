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

    def transfer_to_wallets(self, wallet_id_to, amount,):
        """Transfer among wallets, 0.5% fee"""
        if amount * 1.005 >= self.balance:
            sign = "f"#f for fail
            fee = 0
        else:
            self.balance -= amount * 1.005#0.5% fee
            wallet_id_to.balance += amount
            fee = amount * 0.005
            self.last_transaction = f"Transfer {amount} to wallet({wallet_id_to})"
            sign = "s"#s for success
        return sign, fee#fee will go to the system account


    def transfer_to_other_customers(self, customer, amount):
        """Transfer to others, 1.5% fee, the receiving wallet is arranged according to the number of its' functions"""
        if amount * 1.015 >= self.balance:
            sign = "f"#f for fail
            fee = 0
        else:
            self.balance -= amount * 1.015
            for wallet in customer.wallet_list:
                if wallet.wallet_type == "Daily Use":#4 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sgin = "s"#s for success
                elif wallet.wallet_type == "Holidays":#3 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                elif wallet.wallet_type == "Saving":#2 functions
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
                elif wallet.wallet_type == "Mortgage":#1 function
                    self.balance -= amount * 1.015
                    wallet.balance += amount
                    fee = amount * 0.015
                    self.last_transaction = f"Transfer {amount} to customer({customer.user_name})"
                    sign = "s"#s for success
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

    def transfer_to_wallets(self, wallet_id_to, amount):
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

    def transfer_to_wallets(self, wallet_id_to, amount):
        """Mortgage wallets are not allowed to transfer to other wallet"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee

    def transfer_to_other_customers(self, customer, amount):
        """Mortgage wallets are not allowed to transfer to other customer"""
        sign = "n"#n for not allowed
        fee = 0
        return sign, fee