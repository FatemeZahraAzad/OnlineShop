
import HandleFile
import csv
import logging
from datetime import datetime

class Buy:

    idfc = HandleFile.handleFile('purchase_invoice.csv') 
    file = HandleFile.handleFile('goods.csv')
    def __init__(self,customerName,name_of_store,date=datetime.now()):
        self.customerName = customerName
        self.name_of_store =self.validatin_store(name_of_store)
        self.product_list = []
        self.date = date.date()
        

    def validatin_store(self,store):
        with open('goods.csv','r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if store in i['store']:
                    print("Store name confirmed")
                    break
            return store

    def View_Product_List(self):
        with open('goods.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if self in i['store']:
                        print(f"{i['product_name']} >> from {i['brand']} brand , number of inventory:{i['number_of_inventory']} , expiration date : {i['expiration_date']}")
                        return self
    
    def selection_of_goods(self,*args): #این قسمت برای فاز دوم میباشد
        try:
            with open('goods.csv', 'r') as f :
                r = csv.DictReader(f)
                lst_addr =list(r)
            end = ''                                          #این قسمت باید self بگیرد
            while end != 'yes':
                for i in lst_addr:
                    for productName in args:
                        if productName in i['product_name']:
                            much = input(f' How many {productName} : ')
                            if int(i['number_of_inventory']) > int(much):
                                i['number_of_inventory'] = int(i['number_of_inventory']) - int(much)
                                end = input('Purchase confirmation? (yes/no) ').lower() #!!!!!!!
                                self.product_list.append(f"{productName} : {much}")
                self.file.write_info_user(lst_addr)
            print(self.product_list)
            return self.product_list
        except Exception as e:
            print(e)

    def search_product(self,product):
        with open('goods.csv', 'r') as f:
            r = csv.DictReader(f)
            lst_addr = list(r)
            for i in lst_addr:
                if product in i['product_name']:
                    print(f"{i}")
                    brand = input("what brand do you want? :")
                    if brand in i["brand"]:
                        print(f"{i}")
                        end = input("do you want to buy this good? (yes/no) :").lower()
                        if end == "yes":
                            much = input(f' How many {product} : ')
                            if int(i['number_of_inventory']) > int(much):
                                i['number_of_inventory'] = int(i['number_of_inventory']) - int(much)
                                self.product_list.append(f"{product} {i['brand']} : {much}")
                        else:
                            logging.error("Unsuccessful search")
                            exit(0)
            self.file.write_info_user(lst_addr)
        print(self.product_list)
        return self.product_list

    def saving (self):
        self.idfc.append_info_user(self.__dict__)