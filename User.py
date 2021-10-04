import csv
import logging
from hashlib import sha256
from datetime import datetime, time
from types import coroutine
import HandleFile

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='a',
                    format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")


class Person:
    idfc = HandleFile.handleFile('user.csv')   # in document file csv

    def __init__(self, role, username, password):
        self.role = role
        self.username = self.validation_name(username)
        self.password = self.validation_pasword(password)

    def validation_pasword(self, password):
        if password.isalnum() and len(password) >= 8:
            repeat_password = input("Repeat your password :")
            while repeat_password != password:
                repeat_password = input("Input is incorrect\nRepeat your password again :")
            return sha256(str(repeat_password).encode()).hexdigest()
        else:
            print("invalid password")

    def validation_name(self, name):
        if name.startswith("09") and name.isdigit() and len(name) == 11:
            with open('user.csv', 'r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name not in i['username']:
                        return name
                    else:
                        print("Duplicate name")
                else:
                    return name
        else:
            print("invalid username")

    def saving(self):
        self.idfc.append_info_user(self.__dict__)

    @staticmethod
    def LogIn(username, password):
        try:
            with open('user.csv', 'r') as file:
                filereader = csv.DictReader(file, delimiter=',')
                for i in filereader:
                    if username in i['username'] and sha256(str(password).encode()).hexdigest() in i['password']:
                        if i['role'] == 'customer':
                            logging.info(f"{username} is regester")
                            return "customer"
                        elif i['role'] == 'manager':
                            logging.info(f"{username} is regester")
                            return "manager"
        except Exception as e:
            print(e)

class customer(Person):

    now = datetime.now()
    now_time = str(time(now.hour))

    def __init__(self, role, username, password):
        super().__init__(role, username, password)

    def saving(self):
        self.idfc.append_info_user(self.__dict__)

    @staticmethod
    def checkIn(number,store): #for block customer
        try:
            with open('user.csv', 'r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if i['blacklist']:
                        if store in i['store_name'] and number in i['blacklist']:
                            print(f"You can't enter {i['store_name']} collection")
                            return False
                else:
                    print("Welcome sweety :)")
        except Exception as e:
            print(e)


    @staticmethod
    def show_buy(username):  # فاز دوم_مشاهده لیست خرید های قبلی خود توسط مشتری
        with open('purchase_invoice.csv', 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if username in i['customerName']:
                    print(i)

    @staticmethod
    def show_storeName():
        lst = []
        with open('user.csv', 'r') as file:
            reader = csv.DictReader(file)
            reader2 = list(reader)
            for i in reader2:
                if i['role'] == 'manager':
                    if i['Login_time'] < customer.now_time < i['Exit_time']:
                        lst.append(f"{i['store_name']} : {i['Login_time']} to {i['Exit_time']}")
                        continue
        final_new_menu = list(dict.fromkeys(lst))
        for i in final_new_menu:
            print(i)

    @staticmethod
    def show_goods(store):
        with open('goods.csv', 'r') as file:  # r+
            reader = csv.DictReader(file)
            for i in reader:
                if store in i['store']:
                    print(f"   {i['product_name']} >> {i['brand']} brand | For the price of {i['price']} Toman")
                    continue
        if store == None:
            print()
        else:
            print("The store name entered in the application list is not available")

class Manager(Person):
    idfc = HandleFile.handleFile('user.csv')

    def __init__(self, role, username, password, store_name= None, Login_time=None, Exit_time=None):
        super().__init__(role, username, password)
        self.store_name = store_name
        self.Login_time = Login_time
        self.Exit_time = Exit_time
        self.blacklist = []

    def saving(self):
        self.idfc.append_info_user(self.__dict__)
    @staticmethod
    def show():  # Display customer name
        with open('user.csv', 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if i['role'] == 'customer':
                    print(i['username'])
    @staticmethod
    def show_products(store):  # Show products for the manager
        lst = []
        with open('goods.csv', 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if store in i['store']:
                    print(i)
                    if int(i['number_of_inventory']) <= 10:
                        lst.append(f"{i['product_name']} : {i['number_of_inventory']}")
                        if lst:
                            print()
        print(f"!!!WARNING!!! >> {lst}")
        return (f"!!!WARNING!!! >> {lst}")
    @staticmethod
    def show_buy(shop):  # Purchases made from the manager store
        with open('purchase_invoice.csv', 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if shop in i['store']:
                    print(i)

    def BlackList(self,*args):
        with open('user.csv', 'r') as file:
            reader = csv.DictReader(file)
            lst_adder =list(reader)
            for i in lst_adder:
                for j in args:
                    if j in i['username'] and i['role'] == 'customer':
                        self.blacklist.append(f"{i['username']}")
            self.idfc.write_info_user(lst_adder)
        print(self.blacklist)
        return self.blacklist