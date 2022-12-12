from customer import * 
from wallet import *
from banking_system import *
print("-----Welcome to the banking system!-----")
bank = Banking_system()

while True:
    sign = bank.select_service()
    if sign == "1":
        first_name, last_name, country_of_residence, age, email, password, user_name = bank.input_sign_up_information()
        bank.sign_up(first_name, last_name, country_of_residence, age, email, password, user_name)
        continue##return to the main page by default
    elif sign == "2":
        information_list = bank.input_login_information()
        if information_list == True:#if the username not exist yet and the customer want to go to the main page
            continue
        else:#if the username exist and the customer want to login to the system
            judge = bank.log_in(information_list[0], information_list[1])
            if judge == False:#if the password is incorrect, return to the main page
                continue
            else:#if the password is correct, go to the customer service page
                while True:
                    sign = bank.select_customer_service()
                    customer = bank.customer_dic[information_list[0]]#get the customer object
                    if sign == "1":
                        while True:
                            print("\n-----Select the transaction service:-----")
                            print("1.Deposit")
                            print("2.Withdraw")
                            print("3.Transfer to other wallets")
                            print("4.Transfer to other customers")
                            print("5.Return")
                            print("--------------------------------------")
                            sign = input("Please select your transaction service(using numbers):")
                            if sign == "1":
                                wallet_id = input("Please enter the wallet id:")
                                amount = input("Please enter the amount to deposit:")
                                customer.deposit(wallet_id, amount)
                                continue
                            elif sign == "2":
                                wallet_id = input("Please enter the wallet id to withdraw:")
                                amount = input("Please enter the amount:")
                                customer.withdraw(wallet_id, amount)
                                continue
                            elif sign == "3":
                                wallet_id = input("Please enter the wallet id to transfer from:")
                                wallet_id_to = input("Please enter the wallet id to transfer to:")
                                wallet_to = customer.get_wallet(wallet_id_to)
                                amount = input("Please enter the amount:")
                                fee = customer.transfer_to_wallets(wallet_id, wallet_id_to, amount)
                                bank.system_revenue += fee
                                continue
                            elif sign == "4":
                                wallet_id = input("Please enter the wallet id to transfer from:")
                                customer_name = input("Please enter customer's username to transfer to:")
                                customer_to_transfer = bank.get_customer(customer_name)
                                if customer_to_transfer == False:
                                    print("The customer does not exist! Going back...")
                                    continue
                                else:
                                    amount = input("Please enter the amount:")
                                    fee = customer.transfer_to_others(wallet_id, customer_to_transfer, amount)
                                    bank.system_revenue += fee
                                    continue
                            elif sign == "5":
                                break
                            else:
                                print("Please enter a valid number!")
                                continue
                    elif sign == "2":
                        while True:
                            print("\n-----Select the wallet management service:------")
                            print("1.Create a new wallet(Daily Use, Saving, Holidays, Mortgage)")
                            print("2.Delete a wallet")
                            print("3.Check my wallets")
                            print("4.Return")
                            print("--------------------------------------------")
                            sign = input("Please select your wallet management service(using numbers):")
                            if sign == "1":
                                while True:
                                    print("\n-----Select the wallet type:------")
                                    print("1.Daily Use")
                                    print("2.Saving")
                                    print("3.Holidays")
                                    print("4.Mortgage")
                                    print("--------------------------------------------")
                                    type = input("Please enter the wallet_type(using numbers):")
                                    wallet_id = input("Please enter the wallet id:")
                                    if wallet_id in customer.wallet_id_list:
                                        print("The wallet id already exist! Going back...")
                                        continue
                                    else:
                                        if type == "1":
                                            customer.create_wallet(wallet_id, "Daily Use")
                                            break
                                        elif type == "2":
                                            customer.create_wallet(wallet_id, "Saving")
                                            break
                                        elif type == "3":
                                            customer.create_wallet(wallet_id, "Holidays")
                                            break
                                        elif type == "4":
                                            customer.create_wallet(wallet_id, "Mortgage")
                                            break
                                        else:
                                            print("Please enter a valid type number!")
                                            continue     
                            elif sign == "2":
                                wallet_id = input("Please enter the wallet id:")
                                customer.delete_wallet(wallet_id)
                                continue
                            elif sign == "3":
                                customer.check_my_wallets()
                                continue
                            elif sign == "4":
                                break
                    elif sign == '3':#change password of the customer
                        while True:
                            print("\n-----Select the password change service:------")
                            print("1.Change the password")
                            print("2.Return")
                            print("------------------------------------------")
                            sign = input("Please select your password change service(using numbers):")
                            if sign == "1":
                                old_password = input("Please enter the old password:")
                                new_password = input("Please enter the new password:")
                                if bank.check_password(new_password) == True:
                                    customer.change_password(old_password, new_password)
                                else:
                                    print("invalid password! going back...")
                                    continue
                            elif sign == "2":
                                break
                            else:
                                print("Please enter a valid number!")
                            continue
                    
                    elif sign == '4':#logout...go bank to main page
                        print("-----Logout successfully!-----\n")
                        break
                    else:
                        print("Please enter a valid number!")
                        continue
    elif sign == "3":#exit the system
        print("-----Thank you for using our banking system!-----")
        break
    else:
        print("Please enter a valid number!\n")
        continue