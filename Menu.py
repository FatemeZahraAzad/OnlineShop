import csv
import User
import list_of_stuff
import logging

logging.basicConfig(level=logging.INFO,filename='logs.log',filemode='a',format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")
def menu():  #try exept
    option = 0
    # object1 = HandleFile.handleFile("players_info.csv")
    while option != 3:
        print("1-Sign up")
        print("2-Log in")
        print("3-Exit ")
        option = int(input("choose an option: "))
        if option == 1:
            Role = input("Choose your role (manager/customer): ").lower()
            if Role == "manager":
                logging.info(f"New {Role} is regester")
                username = input("Enter phone number: ") #تکراری نباشه! با این و نات این
                password = input("Enter Password\n(Your password must be above 8 characters and at least one letter):")
                store_name = input("Enter store's name: ")
                Activity_time = input("Enter the time period of your activity(for example : 2018-2020):")
                abject2 = User.Manager(Role,username,password,store_name,Activity_time)
                User.Manager.saving(abject2)
                logging.info(f"{store_name} is regester")
                Registration_of_goods = input("Do you want to register your goods ?!\nEnter yes or no :").lower()
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
                username = input("Enter phone number: ") #تکراری نباشه! با این و نات این
                password = input("Enter Password\n(Your password must be above 8 characters and at least one letter):")
                abject4=User.customer(Role,username,password)
                User.customer.saving(abject4)
            else:
                raise ValueError
        elif option == 2:
            Role = input("Choose your role (manager/customer): ").lower()
            if Role == "manager":
                username = input("Enter your phone number: ") #تکراری نباشه! با این و نات این
                password = input("Enter your Password: ")
                with open('user.csv','r') as file:
                    filereader = csv.DictReader(file, delimiter=',')
                    for i in filereader:
                        if username in i['username'] and password in i['password']: # username in file2 and password in file2:
                            if i['role'] == 'manager':               #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                logging.info(f"{username} is regester")
                                # storeName = input("Enter your store name: ")
                                # list_of_stuff.products.show_products(storeName) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
                                        pass
                                    if choice == 4:
                                        Input2 = "customer"
                                        User.Manager.show(Input2)
                                    if choice == 5:
                                        pass
                            else:
                                print("you are not manager")

            #اسم و پسورد سرچ بشه اگه جز لیست مشتری یا مدیران بود :چاپ کنه که مدیر هستش یا مشتری و دسترسی هاشو نشونش بده
        else:
            print("Invalid input")

menu()