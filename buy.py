
import HandleFile
import csv
import logging
from datetime import datetime

class Buy:

    idfc = HandleFile.handleFile('purchase_invoice.csv') 

    def __init__(self,customerName,nameNumber_of_inventory,name_of_store,date=datetime.now()):
        self.customerName = customerName
        self.name_of_store =name_of_store
        self.nameNumber_of_product = nameNumber_of_inventory
        self.date = date.date()
        

    def validatin_store(self):
            with open('goods.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if self in i['store']:
                        return self

    def View_Product_List(self):
        with open('goods.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if self in i['store']:
                        print(f"{i['product_name']} >> from {i['brand']} brand , number of inventory:{i['number_of_inventory']} , expiration date : {i['expiration_date']}")
                        return self

    def selection_of_good(self,*args): #این قسمت برای فاز دوم میباشد
        lst = []
        with open('goods.csv', 'r') as f :
            r = csv.DictReader(f)
            lst_addr =list(r)
        end = ''                                          #این قسمت باید self بگیرد
        while end != 'yes':
            for i in lst_addr:
                for productName in args:
                    if productName in i['product_name']:
                        much = input(f' How many {productName} : ')
                        i['number_of_inventory'] = int(i['number_of_inventory']) - int(much)
                        end = input('Purchase confirmation? (yes/no) ').lower()
                        lst.append(f"{productName} : {much}")
            self.idfc.write_info_user(lst_addr)
        print(lst)
        return lst

    def show_buy(self):   #فاز دوم_مشاهده لیست خرید های قبلی خود توسط مشتری
            with open('purchase_invoice.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if self in i['customerName']:
                        print(i)

    def saving (self):
            self.idfc.append_info_user(self.__dict__)

# a = Buy.validatin_store("Ofogh")
# b = Buy.selection_of_good()
# c = Buy("09191049849",a,b) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# c.saving()