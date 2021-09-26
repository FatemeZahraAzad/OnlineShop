import HandleFile
import csv
import logging

class Buy:

    idfc = HandleFile.handleFile('goods.csv') 
    file = HandleFile.handleFile('purchase_invoice.csv')

    def __init__(self,customerName,name_of_product,number_of_inventory,name_of_store):
        self.customerName = customerName
        self.name_of_product = name_of_product
        self.number_of_inventory = number_of_inventory
        self.name_of_store =self.validatin_store(name_of_store)

    def validatin_store(self,nos): # nos stands for name_of_store
            with open('goods.csv','r') as file:         #Purchase_Invoice.csv      factore kharid
                reader = csv.DictReader(file)
                for i in reader:
                    if nos in i['store']:
                        return nos
                        # print(f"{i['product_name']} >> from {i['brand']} brand , number of inventory:{i['number_of_inventory']} , expiration date : {i['expiration_date']}")
                        # select = ''
                        # while select != 'no':
                        #     select = input('Enter the name of one of the items (otherwise enter no) :').lower().strip()
                        #     with open('goods.csv','r') as file2:         #Purchase_Invoice.csv      factore kharid
                        #         reader = csv.DictReader(file2)
                        #         for i in reader:
                        #             if select in i['product_name']:
                        #                 print('The purchase was successful')
    
    def View_Product_List(self,nos):
        with open('goods.csv','r') as file:         #Purchase_Invoice.csv      factore kharid
                reader = csv.DictReader(file)
                for i in reader:
                    if nos in i['store']:
                        print(f"{i['product_name']} >> from {i['brand']} brand , number of inventory:{i['number_of_inventory']} , expiration date : {i['expiration_date']}")

    def show_buy(self,name):
            with open('purchase_invoice.csv.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name in i['customerName']:
                        print(i)

    def saving (self):
            self.idfc.append_info_user(self.__dict__)