# -*- coding: utf-8 -*-
"""
Created on Tues Dec 13 16:21:00 2022

@ author: Jinyu Meng(sw22365@bristol.ac.uk)
The banking system mainly contains the following functions:
1.sign up: which is used to create a new account.
2.log in: which is used to log in the system.
3.select service: which is used to select the service before log in.
4.select customer service: which is used to select the service after log in.
5.input sign up information: which is used to input the information of sign up.
6.input login information: which is used to input the information of log in.
7.check word: which is used to check if the word is valid.
8.check age: which is used to check if the number is valid.
9.check email: which is used to check if the email is valid.
10.check password: which is used to check if the password is valid.
11.check user name: which is used to check if the user name is valid.
"""

from customer import *
from wallet import *
from email.utils import parseaddr
import re

class Banking_system:
    """The bank class"""
    def __init__(self):
        """Initialize the banking system"""
        self.customer_dic = {}
        self.system_revenue = 0
        self.customer_service = ("Transactions","Wallet Management","Change Password","Log out")
        self.service = ("Sign up","Log in","Exit")

    def get_customer(self, user_name):
        """Get the customer object"""
        if user_name in self.customer_dic:
            return self.customer_dic[user_name]
        else:
            return False

    def select_customer_service(self):
        "select the services after login"
        print("\n-----Select your service:-----")
        for i, service in enumerate(self.customer_service):
            print(f"{i+1}.{self.customer_service[i]}")
        sign = input("Please select your service:")
        return sign
    
    def select_service(self):
        """Select the services before login"""
        print("\n-----Select banking services:-----")
        for i, service in enumerate(self.service):
            print(f"{i+1}.{self.service[i]}")
        sign = input("Please select your service(using numbers):")
        return sign

    def input_sign_up_information(self):
        """Input the information of sign up"""
        while True:
            first_name = input("Please enter your first name:")
            if self.check_word(first_name) == False:
                print("Please enter a valid first name!")
                continue
            else:
                break
        while True:
            last_name = input("Please enter your last name:")
            if self.check_word(last_name) == False:
                print("Please enter a valid last name!")
                continue
            else:
                break
        while True:
            country_of_residence = input("Please enter your country of residence:")
            if self.check_word(country_of_residence) == False:
                print("Please enter a valid country of residence!")
                continue
            else:
                break
        while True:
            age = input("Please enter your age:")
            if self.check_age(age) == False:
                print("Please enter a valid age!")
                continue
            else:
                break
        while True:
            email = input("Please enter your email:")
            if self.check_email(email) == False:
                print("Please enter a valid email!")
                continue
            else:
                break
        while True:
            password = input("Please enter your password(using numbers and letters in both lowercase and uppercase, longer than 8):")
            if self.check_password(password) == False:
                print("Please enter a valid password!")
                continue
            else:
                break
        while True:
            user_name = input("Please enter your user name(using numbers and letters in both lowercase and uppercase, longer than 8):")
            if user_name in self.customer_dic.keys():#username is the unique key
                print("Please enter a valid user name!")
                continue
            if self.check_user_name(user_name) == False:
                print("Please enter a valid user name! (probably exists)")
                continue
            else:
                break
        return first_name, last_name, country_of_residence, age, email, password, user_name
    
    def input_login_information(self):
        """Input the information of log in"""
        while True:
            user_name = input("Please enter your user name:")
            if user_name not in self.customer_dic.keys():
                decision = input("We can't find your user name! Enter 'y' to return to main page or 'n' to enter again:")
                if decision == 'y':
                    return True
                else:
                    continue
            else:
                password = input("Please enter your password:")
                information_list = [user_name, password]
                return information_list
           
    def check_word(self, word):
        """Check if the word is valid"""
        if word.isalpha() == False:
            return False
        else:
            return True
    
    def check_age(self, number):
        """Check if the number is valid"""
        if number.isdigit() == False:
            return False
        if int(number) < 0 or int(number) > 120:
            return False
        else:
            return True
    
    def check_email(self, email):
        """Check if the email is valid"""
        email_tuple = parseaddr(email)
        if email_tuple[1] == '' or '@' not in email_tuple[1]:
            return False
        else:
            return True
    
    def check_password(self, password):
        """Check if the password is valid"""
        lower = re.compile('[a-z]')
        upper = re.compile('[A-Z]')
        digit = re.compile('[0-9]')
        wrong = re.compile('[^a-zA-Z0-9]')

        if len(password) < 8 or wrong.search(password) != None:
            return False
        elif lower.search(password) != None and upper.search(password) != None and digit.search(password) != None:
            return True
        else:
            return False
        
    def check_user_name(self, user_name): 
        """Check if the user name is valid"""
        lower = re.compile('[a-z]')
        upper = re.compile('[A-Z]')
        digit = re.compile('[0-9]')
        wrong = re.compile('[^a-zA-Z0-9]')
        if user_name in self.customer_dic.keys():
            return False
        if len(user_name) < 8 or wrong.search(user_name) != None:
            return False
        elif lower.search(user_name) != None and upper.search(user_name) != None and digit.search(user_name) != None:
            return True
        else:
            return False

    def check_system_revenue(self):
        """Check the system revenue"""
        print("The system revenue is: ", self.system_revenue)

    def sign_up(self, first_name, last_name, country_of_residence, age, email, password, user_name):
        """Sign up a new customer"""
        self.customer_dic[user_name] = Customer(first_name, last_name, country_of_residence, age, email, password, user_name)
        print("-----Sign up successfully!-----")

    def log_in(self, user_name, password):
        """Log in a customer"""
        if self.customer_dic[user_name].password == password:
            print("-----Log in successfully!-----\n")
            return True 
        else:
            print("Log in failed! Going bank to main page...")
            return False