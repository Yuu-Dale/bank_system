from customer import * 
from wallet import *

Dale = Customer(1,2,3,4,5,6,7)
Dale.create_wallet('Dale_wallet_1', 'Daily use')
Dale.create_wallet("Dale_wallet_2", "Saving")
Dale.create_wallet("Dale_wallet_3", "Holidays")
Dale.create_wallet("Dale_wallet_4", "Mortgage")
print(Dale.wallet_list)
Dale.deposit("Dale_wallet_1",100)
Dale.deposit("Dale_wallet_2",100)
Dale.deposit("Dale_wallet_3",100)
Dale.deposit("Dale_wallet_4",100)
Dale.check_my_wallets()
Dale.transfer_to_wallets("Dale_wallet_1", "Dale_wallet_2", 50)
Dale.check_my_wallets()
Dale.transfer_to_wallets("Dale_wallet_3", "Dale_wallet_4", 50)
