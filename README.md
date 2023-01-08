# sw22365_EMATM0048
Part1 Software Development.

There are 4 documents in this part which are main.py, banking_system.py, customer.py and wallet.py.

We use the following structure to store the data, firstly once "main.py" is run an instance of the banking system is created, the system instance has the ability to create instances of customers, which are stored in a dictionary in the banking system called "customer_dic The customer instance has the ability to create wallet instances, which are stored in a dictionary called "customer_dic", the key of which is the username that was entered when the customer was created. The created wallet instances are stored in a list called "wallet_list" for the corresponding customer instance.

"Main.py" is used to call functions from other files. When you run "main.py" you are asked to select a banking service: 1 for "sign up", 2 for "log in” and 3 for "exit". When you choose 1, then you are asked to fill some information about your account. If you choose 2, you are asked to log in by using your username and password. Then you can continue using further services. If you choose 3, you will exit this banking system.

Once you have successfully logged in you can use the corresponding numbers to select the functions "transactions", "wallet management", "change password" and "log out". In the "Transactions" section you can select "deposit", "withdraw", "transfer to other wallets", "transfer to other customers" and "return" these five functions; in 'wallet management' section, you can create a new wallet (Daily Use, Saving, Holidays, Mortgage), "delete a wallet", "check my wallets" and "return", and in "create a new wallet' you can select the type of wallet you want to create using the corresponding number; in the "change password" section, it includes two functions "change the password" and "return" ; in "log out" section, you can log out and return to the login page automatically.

"banking system.py" contains functions of a "banking system" instance, which mainly contains the following functions:
1.sign up: which is used to create a new customer with first_name, last_name, country_of_residence, age, email, password and user_name.
2.log in: which is used to log in the system with user_name and password.
3.select service: which is used to select the service before log in, different numbers represent for different service.
4.select customer service: which is used to select the service after log in,different numbers represent for different service.
5.input sign up information: which is used to receive the information of sign up.
6.input login information: which is used to receive the information of log in.
7.check word: which is used to check if the word is valid.
8.check age: which is used to check if the number is valid.
9.check email: which is used to check if the email is valid.
10.check password: which is used to check if the password is valid.
11.check user name: which is used to check if the user name is valid.

"customer.py" contains functions of a "customer" instance, which mainly contains the following functions:
1.get wallet: which is used to get a wallet by wallet id.
2.create wallet: which is used to create a wallet for customer by wallet_id and amount.
3.delete wallet: which is used to delete a wallet for customer by wallet_id.
4.change password: which is used to change the password of customer by giving old password and new password.
5.deposit: which is used to deposit money into a wallet by wallet_id and amount.
6.withdraw: which is used to withdraw money from a wallet by wallet_id and amount.
7.transfer to wallets: which is used to transfer money from one wallet to another wallet of the same customer by wallet_id_from, wallet_id_to and amount. When the wallet’s balance is not sufficient you can choose whether to find a alternative wallet.
8.transfer to other customers: which is used to transfer money from one wallet to another wallet of other customers by wallet_id_from, customer and amount. When the wallet’s balance is not sufficient you can choose whether to find a alternative wallet.
9.find substitution yourself: which is used to find a substitution for the customer when the customer transfer money to other wallet of himself, and the wallet is not enough by wallet_id_from, wallet_to, amount. But when you have to call this function, it is bundled with function 7th.
10.find substitution for other customers: which is used to find a substitution for the customer when the customer transfer money to other wallet of other customers, and the wallet is not enough by wallet_id_from, customer, amount. But when you have to call this function, it is bundled with function 8th.

"wallet.py"contains functions of a "wallet" instance, which mainly contains the following functions:
1.deposit: which is used to deposit money by amount.
2.withdraw: which is used to withdraw money by amount.
3.transfer to wallets: which is used to transfer money to other wallets of the same customer by wallet_to and amount.
4.transfer to other_customers: which is used to transfer money to other customers by customer and amount.

Part 2: Data Analytics

In this section, I use the API of yahoo finance by installing "yahoo_fin.stock_info" package and follow the guide on yahoo official website to use their data.

I use "scipy.stats" package to calculate the Pearson coefficient which can return correlation coefficient and p-value by giving two variables.

I use "scikit-learn" package to use linear-regression model and train the model using the train data set. Then I use the trained model to predict the value of the test data set.

I use "tslearn" which is a Python package that provides machine learning tools for the analysis of time series. This package builds on (and hence depends on) scikit-learn, numpy and scipy libraries. I mainly use "K-shape" Clustering.

I use "statsmodels" package, which is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. An extensive list of result statistics are available for each estimator. The results are tested against existing statistical packages to ensure that they are correct. The package is released under the open source Modified BSD (3-clause) license. And I use it to make "t-test", decide p and q for "ARIMA" model and use the "ARIMA" model.
