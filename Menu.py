import csv
import User
import list_of_stuff
import logging
import buy
import search

logging.basicConfig(level=logging.INFO,filename='logs.log',filemode='a',format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")

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
                        password = input("Enter Password\n(Your password must be above 8 characters and at least one letter):")
                        store_name = input("Enter store's name: ")
                        Activity_time = input("Enter the time period of your activity(for example : 2018-2020):")
                        abject2 = User.Manager(Role,username,password,store_name,Activity_time)
                        User.Manager.saving(abject2)
                        logging.info(f"{store_name} is regester")
                        Registration_of_goods = input("Do you want to register your goods ?!\nEnter yes or no :").lower().strip()
                        if Registration_of_goods == "yes":
                            print(f"welcome sir\nThank you for choosing our application\nPlease enter the requested information")
                            Input = ''
                            while Input != 'no':
                                store = input("store name >> ").lower()
                                barcode = input("Barcode of goods >> ")
                                price = input("Price of gooods >> ")
                                brand = input("Brand of goods >> ").lower()
                                product_name = input("Product name of goods >> ").lower()
                                number_of_inventory = input("Number of inventory >> ")
                                expiration_date = input("Expiration date of goods >> ")
                                abject3 = list_of_stuff.products(store,barcode,price,brand,product_name,number_of_inventory,expiration_date)
                                list_of_stuff.products.saving(abject3)
                                logging.info(f"{product_name} is regester")
                                Input = input("Do you still want to register a product?\nIf you don't want to enter the word ""no"" : ").lower()
                    elif Role == "customer":
                        logging.info(f"New {Role} is regester")
                        username = input("Enter phone number: ")
                        password = input("Enter Password\n(Your password must be above 8 characters and at least one letter):")
                        abject4=User.customer(Role,username,password)
                        User.customer.saving(abject4)
                    else:
                        logging.error(ValueError)
                        raise ValueError
                except Exception as e:
                    print("please choise manager or customer ")
                    logging.error("Failed to register")
                    continue
            elif option == 2:
                try:
                    Role = input("Choose your role (manager/customer): ").lower()
                    if Role == "manager":
                        username = input("Enter your phone number: ")
                        password = input("Enter your Password: ")
                        with open('user.csv','r') as file:
                            filereader = csv.DictReader(file, delimiter=',')
                            for i in filereader:
                                if username in i['username'] and password in i['password']: # username in file2 and password in file2:
                                    if i['role'] == 'manager':
                                        logging.info(f"{username} is regester")
                                        choice = 0
                                        while choice != 3 :
                                            print("1-View store inventory")
                                            print("2-View customer purchase invoice")
                                            print("3-Invoice Search ")
                                            print("4-View the profile list of all customers ")
                                            print("5-Customer block ")
                                            print("6-Exit ")
                                            choice = int(input("choose an number: "))
                                            if choice == 1:
                                                NameStore = input("Enter your store name :").lower()
                                                abject5=list_of_stuff.products.show_products(NameStore)
                                                list_of_stuff.products.validation_inventory(abject5)
                                            if choice == 2:
                                                Name_Store = input("Enter your store name :").lower()
                                                list_of_stuff.products.show_buy(Name_Store)
                                            if choice == 3:
                                                type = input("On what basis do you want to search?\n(enter -> customer or date):").lower()
                                                search.Search.search_manager(type)
                                            if choice == 4:
                                                Input2 = "customer"
                                                User.Manager.show(Input2)
                                            if choice == 5:
                                                pass
                                    else:
                                        print("you are not manager")
                                        logging.error("Failed log in")
                    elif Role == 'customer':
                        username = input("Enter your phone number: ")
                        password = input("Enter your Password: ")
                        with open('user.csv','r') as file:
                            filereader = csv.DictReader(file, delimiter=',')
                            for i in filereader:
                                if username in i['username'] and password in i['password']:
                                    logging.info(f"{username} is regester")
                                    choice2 = 0
                                    while choice2 != 3 :
                                        print("1-View your previous invoices") #مشاهده فاکتور قبلی
                                        print("2-Show list of stores") #نمایش لیستی از فروشگاه ها
                                        print("3-Store Search") #جست و جوی فروشگاه
                                        print("4-Select a store") #انتخاب فروشگاه
                                        print("5-View Product List") #مشاهده لیست کالا ها
                                        print("6-Selection of goods") #انتخاب اجناس
                                        print("7-View pre-invoice") #مشاهده پیش فاکتور
                                        print("8-Confirm purchase or edit it") #تایید خرید یا ویرایش ان
                                        print("9-Exit")
                                        choice2 = int(input("choose an number: "))
                                        if choice2 == 1:
                                            pass
                                        if choice2 == 2:
                                            pass
                                        if choice2 == 3:
                                            pass
                                        if choice2 == 4:
                                            pass
                                        if choice2 == 5:
                                            View_of_good = input("Enter your store name :")
                                            shop = buy.Buy.View_Product_List(View_of_good)
                                            select_of_good = input("Do you want to select a goods ?!\nEnter yes or no :").lower()
                                            if select_of_good == 'yes':
                                                name = ''
                                                nummmber = ''
                                                while name and nummmber != 'done':
                                                    name,nummmber = input('enter your choise and nomber of its\nfor example ->  candy,5 \notherwise enter done,done ').lower().strip().split(',')
                                                nop = buy.Buy.selection_of_good(name = nummmber) #!!!!!!! این قسمت برای فاز دوم میباشد
                                            factore=buy.Buy(username,shop,nop)
                                            buy.Buy.saving(factore)
                                        if choice2 == 7:
                                            pass
                                        if choice2 == 8:
                                            pass
                except Exception as e:
                    logging.error(ValueError)
                    print(e)
                    continue
        except Exception as e:
            print(e)
            logging.error(ValueError)
            
menu()