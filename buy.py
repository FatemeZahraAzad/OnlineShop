import HandleFile
import csv
import logging
from datetime import datetime

class Buy:

    idfc = HandleFile.handleFile('purchase_invoice.csv') 

    def __init__(self,customerName,nameNumber_of_inventory,name_of_store,date=datetime.now()):
        self.customerName = customerName
        self.nameNumber_of_product = nameNumber_of_inventory
        self.name_of_store =name_of_store
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

    def selection_of_good(**kwargs): #این قسمت برای فاز دوم میباشد
        lst = []
        with open('goods.csv','r+') as file2:
            reader2 = csv.DictReader(file2)
            for i in reader2:
                for key, value in kwargs.items():
                    if key in i['product_name'] and int(i['number_of_inventory']) >= int(value) :
                        lst.append(f"{key} : {value}")
                        newNumber= int(i['number_of_inventory']) - int(value)
                        i['number_of_inventory'] = newNumber
        print(lst)
        return lst

    def show_buy(self,name):
            with open('purchase_invoice.csv.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name in i['customerName']:
                        print(i)

    def saving (self):
            self.idfc.append_info_user(self.__dict__)

# a = Buy.validatin_store("Ofogh")
# b = Buy.selection_of_good(shoes= 3 ,chokolate = 3 ,candy=3)
# print(b)
# c = Buy("09191049849",b,a)
# c.saving()