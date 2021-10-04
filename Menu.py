import logging
import os
from datetime import time
import User
import buy
import list_of_stuff
from search import Search

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='a',
                    format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")

def menu():
    option = 0
    while option != 3:
        print("1-Sign up")
        print("2-Log in")
        print("3-Exit ")
        try:
            option = int(input("choose an option: "))
            if option == 1:
                try:
                    Role = input("Choose your role (manager/customer): ").lower().strip()
                    if Role == "manager":
                        logging.info(f"New {Role} is regester")
                        username = input("Enter phone number: ")
                        password = input(
                            "Enter Password\n(Your password must be above 8 characters and at least one letter):")
                        store_name = input("Enter store's name: ")
                        login_time = str(time(int(input("Enter Your Log in hour:"))))
                        Exit_time = str(time(int(input("Enter Your exit hour:"))))
                        abject2 = User.Manager(Role, username, password, store_name, login_time, Exit_time)
                        User.Manager.saving(abject2)
                        logging.info(f"{store_name} is regester")
                        os.system('cls')
                        Registration_of_goods = input(
                            "Do you want to register your goods ?!\nEnter yes or no :").lower().strip()
                        if Registration_of_goods == "yes":
                            print(
                                f"welcome sir\nThank you for choosing our application\nPlease enter the requested information")
                            Input = ''
                            while Input != 'no':
                                store = input("store name >> ").lower()
                                barcode = input("Barcode of goods >> ")
                                price = input("Price of gooods >> ")
                                brand = input("Brand of goods >> ").lower()
                                product_name = input("Product name of goods >> ").lower()
                                number_of_inventory = input("Number of inventory >> ")
                                expiration_date = input("Expiration date of goods >> ")
                                abject3 = list_of_stuff.products(store, barcode, price, brand, product_name,
                                                                 number_of_inventory, expiration_date)
                                list_of_stuff.products.saving(abject3)
                                logging.info(f"{product_name} is regester")
                                os.system('cls')
                                Input = input(
                                    "Do you still want to register a product?\nIf you don't want to enter the word ""no"" : ").lower()
                            os.system('cls')

                            # show meno # TODO

                    elif Role == "customer":
                        logging.info(f"New {Role} is regester")
                        username = input("Enter phone number: ")
                        password = input(
                            "Enter Password\n(Your password must be above 8 characters and at least one letter):")
                        abject4 = User.customer(Role, username, password)
                        User.customer.saving(abject4)
                        os.system('cls')

                        # show meno  # TODO

                    else:
                        logging.error(ValueError)
                        raise ValueError
                except Exception as e:
                    print("please choise manager or customer ")
                    logging.error("Failed to register")
                    continue
            elif option == 2:
                username = input("Enter your phone number: ")
                password = input("Enter your Password: ")
                Copyname = username
                name = username
                Copy_name = username
                copy_name = username
                copy_password = password
                abject1 = User.Person.LogIn(username, password)
                copy_roll = abject1
                if abject1 == "manager":
                    choice = 0
                    while choice != 7:
                        print("1-Registration of new goods")
                        print("2-View store inventory")
                        print("3-View customer purchase invoice")
                        print("4-Invoice Search ")
                        print("5-View the profile list of all customers ")
                        print("6-Customer block ")
                        print("7-Exit ")
                        choice = int(input("choose an number: "))
                        if choice == 1:
                            Input = ''
                            while Input != 'no':
                                store = input("store name >> ").lower()
                                barcode = input("Barcode of goods >> ")
                                price = input("Price of gooods >> ")
                                brand = input("Brand of goods >> ").lower()
                                product_name = input("Product name of goods >> ").lower()
                                number_of_inventory = input("Number of inventory >> ")
                                expiration_date = input("Expiration date of goods >> ")
                                abject3 = list_of_stuff.products(store, barcode, price, brand, product_name,
                                                                 number_of_inventory, expiration_date)
                                list_of_stuff.products.saving(abject3)
                                logging.info(f"{product_name} is regester")
                                os.system('cls')
                                Input = input(
                                    "Do you still want to register a product?\nIf you don't want to enter the word ""no"" : ").lower()
                        if choice == 2:
                            store = input("Enter store name")
                            User.Manager.show_products(store)
                            # print()
                        if choice == 3:
                            store = input("Enter store name")
                            User.Manager.show_buy(store)
                        if choice == 4:
                            invoice = input("Search (for example 09123456789 2021-1-1):")
                            Search.search_manager(invoice)
                        if choice == 5:
                            User.Manager.show()
                        if choice == 6:
                            thing4 = User.Manager(copy_roll,copy_name,copy_password)
                            block = input("Enter his/her number:")
                            thing4.BlackList(block)
                if abject1 == "customer":
                    User.customer.show_buy(name)
                    name2 = username
                    choice2 = 0
                    while choice2 != 3:
                        print("1-Display store names")
                        print("2-Search the store name")
                        choice2 = int(input("choose an number: "))
                        if choice2 == 1:
                            User.customer.show_storeName()
                            StoreName = input("Select one of the stores and enter its name : ")
                            CopyStore = StoreName
                            copynumber = username
                            result = User.customer.checkIn(copynumber,CopyStore)
                            if result != False:
                                copy_store = StoreName
                                Copy_store = StoreName
                                ####################################
                                object4 = buy.Buy(name2, StoreName)
                                choice3 = 0
                                while choice3 !=2:
                                    print("1-Display goods")
                                    print("2-Search the goods")
                                    choice3 = int(input("choose an number: "))
                                    if choice3 == 1:
                                        User.customer.show_goods(copy_store)
                                        choice_product = input("Select a good : ")
                                        object5 = object4.selection_of_goods(choice_product)
                                        Confirmation = input("Are you finalizing your purchase ?!\n(yes or no) >> ")
                                        if Confirmation == "no":
                                            Exit = input("Do you want to get out ?!\n(yes/no): ")
                                            if Exit == "yes":
                                                exit(0)
                                            if Exit == "no":
                                                exit(1)
                                        if Confirmation == "yes":
                                            object4.saving()
                                        else:
                                            print(161)
                                    if choice3 == 2:
                                        instance = buy.Buy(Copy_name,Copy_store)
                                        end = ''
                                        while end != "no":
                                            search = input("search is ready: ")
                                            instance.search_product(search)
                                            end = input("Do you want to search again ?! ").lower()
                                        Confirmation2 = input("Are you finalizing your purchase ?!\n(yes or no) >> ")
                                        if Confirmation2 == "no":
                                            Exit2 = input("Do you want to get out ?!\n(yes/no): ")
                                            if Exit2 == "yes":
                                                exit(0)
                                            if Exit2 == "no":
                                                exit(1)
                                        if Confirmation == "yes":
                                            instance.saving()
                        if choice2 == 2:
                            search1 = input("search is ready: ")
                            search_store = Search.search_customer(search1)
                            copystore = search_store
                            User.customer.show_goods(search_store)
                            object6 = buy.Buy(name2,copystore)
                            object7 = ''
                            while object7 != 'no':
                                shop = object6.selection_of_goods(input("what do you want?! :"))
                                object7 = input("do you ant more?! ").lower()
                            object6.saving()                            
                else:
                    print("Your name was not found. Please register first")
                    logging.error("Failed log in")
        except Exception as e:
            print(e)
menu()
