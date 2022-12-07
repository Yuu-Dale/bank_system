from customer import *
from wallet import *

def sign_up():
    user_name = input("Please enter your username:")
    active = True
    while active:
        '''Check if the user name has been used'''
        if user_name in user_name_dic.keys():
            print("This user name has been used, please choose another one.")
            '''Ask the customer whether to quit or not'''
            letter = input("Do you want to continue or not(y/n)")
            if letter.lower() == "y":
                sign_up()
            else: ##We don't care if the customer does not enter 'y'
                active = False
        else:
            password = input("Please enter your password:")
            user_name_dic['user_name'] = password
            active = False
        print("------Sign-up process has finished------")


def login():
    user_name = input("Please enter your user_name:")
    active = True
    while active:
        if user_name in user_name_dic.keys():
            password = input("Please enter your password:")
            if user_name_dic['user_name'] == password:
                pass
        else:
            print("This email address does not exist")
            letter = input("Do you want to continue or not(y/n)")
            if letter.lower() == "y":
                login()
            else:  ##We don't care if the customer does not enter 'y'
                active = False
    print("------Login process has finished------")



