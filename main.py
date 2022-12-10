from customer import * 
from wallet import *

Dale = Customer(1,2,3,4,5,6,7)
Mary = Customer(8,7,6,5,4,3,2)
s, Dale_wallet_1 = Dale.create_wallet('Dale_wallet_1', 'Daily use')
s, Dale_wallet_2 = Dale.create_wallet("Dale_wallet_2", "Saving")
#Dale.delete_wallet("Dale_wallet_2")
s, Dale_wallet_3 = Dale.create_wallet("Dale_wallet_3", "Holidays")
s, Dale_wallet_4 = Dale.create_wallet("Dale_wallet_4", "Mortgage")
s, Dale_wallet_5 = Dale.create_wallet('Dale_wallet_5', 'Daily use')


s, Mary_wallet_1 = Mary.create_wallet('Mary_wallet_1', 'Daily use')
s, Mary_wallet_2 = Mary.create_wallet('Mary_wallet_2', 'Saving')
s, Mary_wallet_3 = Mary.create_wallet('Mary_wallet_3', 'Holidays')
s, Mary_wallet_4 = Mary.create_wallet('Mary_wallet_4', 'Mortgage')
#Dale.delete_wallet("Dale_wallet_5")
print(Dale.wallet_list)
Dale.deposit("Dale_wallet_1",50)
Dale.deposit("Dale_wallet_2",100)
Dale.deposit("Dale_wallet_3",50)
Dale.deposit("Dale_wallet_4",100)
Dale.deposit("Dale_wallet_5",500)
Dale.transfer_to_others("Dale_wallet_1", Mary, 10)#成功
Dale.transfer_to_others("Mary_wallet_1", Mary, 10)#不是dale的钱包
Dale.transfer_to_others("Dale_wallet_1", Mary, 100)#钱不够
Dale.transfer_to_others("Dale_wallet_2", Mary, 10)#没权限
Dale.check_my_wallets()
Mary.check_my_wallets()
