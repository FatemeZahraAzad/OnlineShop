# import HandleFile
import csv
# class products:
#     idfc = HandleFile.handleFile('goods.csv')
#     def __init__(self,barcode,price,brand,product_name,number_of_inventory,expiration_date): #بارکد,قیمت,برند,نام کالا,تعداد موجودی,تاریخ انقضا
#         self.barcode=barcode
#         self.price=price
#         self.brand=brand
#         self.product_name=product_name
#         self.number_of_inventory=self.validation_inventory(number_of_inventory)
#         self.expiration_date=expiration_date

#     def validation_inventory(self,noi): # noi stands for number of inventory
#         lst = []
#         with open('goods.csv','r') as file:
#                 reader = csv.DictReader(file)
#                 reader2 = list(reader)
#                 for i in reader2:
#                     # if int(i['number_of_inventory']) <= 10:
#                     if noi in i['number_of_inventory'] and int(noi) <= 10: #!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                         lst2 = lst.append(noi)
#                         print(lst2)
#                         return lst2
#                     # if int(noi) <= 10:
#                         # return "! Less than 10 are left !"
#                     else:
#                         return noi

#     def buy(self):
#         #Purchase_Invoice.csv      factore kharid
#         pass

#     def saving (self):
#         self.idfc.append_info_user(self.__dict__)
    
#     def show_products(self):
#         with open('goods.csv','r') as file:
#             reader = csv.DictReader(file)
#             for i in reader:
#                 print(i)
                
#     def show_buy(self):
#         with open('purchase_invoice.csv.csv','r') as file:
#             reader = csv.DictReader(file)
#             for i in reader:
#                 print(i)
# a = products("123456789","4500","yumi","chokolate","15","2020.11.9")
# a.saving()
# b =products("123456789","4500","yumi","chokolate","9","2020.11.9")
# b.saving()
# c = products("123456789","4500","yumi","chokolate","1","2020.11.9")
# c.saving()

# lst = []
# with open('goods.csv','r') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             if int(i['number_of_inventory']) <= 10:
#                 lst.append(f"{i['product_name']} : {i['number_of_inventory']}")
#         print(lst)  ##!!!!!!!!!!!!!!!!!!! ,, check

def show():
    with open('user.csv','r') as file:
        reader = csv.DictReader(file)
        for i in reader:
            if i['role'] == 'customer': #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                print(i['username'])
show()