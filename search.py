import csv


class Search:
    def search_manager (type) :
        try:
            with open('purchase_invoice.csv','r') as file:   # r+
                reader = csv.DictReader(file)
                for i in reader:
                    if type == f"{i['customerName']} {i['date']}":
                        print(i)



















        #                 choise = input("Are you looking for a specific person invoice?\n(enter yes or no) :")
        #                 if choise == "no":
        #                     store = input("please enter your store name :").strip()
        #                     with open('purchase_invoice.csv','r') as file:
        #                         reader = csv.DictReader(file)
        #                         for i in reader:
        #                             if store in i['name_of_store']:
        #                                 print(i)
        #                             else:
        #                                 print("No purchase from your store yet")
        #                 elif choise == "yes":
        #                     customerName = input("enter his/her number: ")
        #                     store1 = input("please enter your store name :").strip()
        #                     with open('purchase_invoice.csv','r') as file:
        #                         reader = csv.DictReader(file)
        #                         for i in reader:
        #                             if store1 in i['name_of_store'] and customerName in i['customerName']:
        #                                 print(i)
        #                 else:
        #                     print("Invalid input")
        #             if type == "date":
        #                 choise2 = input("Are you looking for a specific date?\n(enter yes or no) :").lower().strip()
        #                 if choise2 == "no":
        #                     store2 = input("please enter your store name :").strip()
        #                     with open('purchase_invoice.csv','r') as file:
        #                         reader = csv.DictReader(file)
        #                         for i in reader:
        #                             if store2 in i['name_of_store']:
        #                                 print(i)
        #                 elif choise2 == "yes":
        #                     date = input("enter date (for example : 2021-01-1): ")
        #                     store1 = input("please enter your store name :").strip()
        #                     with open('purchase_invoice.csv','r') as file:
        #                         reader = csv.DictReader(file)
        #                         for i in reader:
        #                             if store1 in i['name_of_store'] and date in i['date']:
        #                                 print(i)
        #                             else:
        #                                 print("The requested date was not found")
        #                 else:
        #                     print("Invalid input")
        except Exception as e:
            print(e)
     
# a = Search.search_manager("customer")
#__________________________________________________________________________________________________________________

# a = Search.search_manager("date")
