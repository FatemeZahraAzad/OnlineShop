import csv

# def selection_of_good(**kwargs): #این قسمت برای فاز دوم میباشد
#         lst = []
#         with open('goods.csv','r+') as file2:
#             reader2 = csv.DictReader(file2)
#             writer = csv.DictWriter(file2)
#             for i in reader2:
#                 for key, value in kwargs.items():
#                     if key in i['product_name'] and int(i['number_of_inventory']) >= int(value) :
#                         newNumber= int(i['number_of_inventory']) - int(value)
#                         i['number_of_inventory'] = newNumber
#                     lst.append(f"{key} : {value}")

#         print(lst)
#         return lst
# selection_of_good(shoes = 3 , candy = 3 , chokolate = 3)


import HandleFile

def edite_address(self):
    lst = []
    with open('goods.csv', 'r') as f :
        r = csv.DictReader(f)
        lst_addr =list(r)
    end = ''
    while end != 'yes':
        for i in lst_addr:
            if self in i['product_name']:
                much = input(' how much: ')
                i['number_of_inventory'] = int(i['number_of_inventory']) - int(much)
                end = input('Purchase confirmation? (yes/no) ').lower()
                lst.append(f"{self} : {much}")
        self.idfc.write_info_user(lst_addr)
    print(lst)
    return lst 

idfc = HandleFile.handleFile('goods.csv')
edite_address("shoes")

# import HandleFile
# import csv
# class A:

#     idfc = HandleFile.handleFile('goods.csv')

#     def __init__(self,store,barcode,price,brand,product_name,number_of_inventory,expiration_date): #بارکد,قیمت,برند,نام کالا,تعداد موجودی,تاریخ انقضا
#             self.store = store
#             self.barcode=barcode
#             self.price=price
#             self.brand=brand
#             self.product_name=product_name
#             self.number_of_inventory = number_of_inventory
#             self.expiration_date=expiration_date

#     def selection_of_good(**kwargs): #این قسمت برای فاز دوم میباشد
#         lst = []
#         with open('goods.csv','r+') as file2:
#             reader2 = csv.DictReader(file2)
#             for i in reader2:
#                 for key, value in kwargs.items():
#                     if key in i['product_name'] and int(i['number_of_inventory']) >= int(value) :
#                         lst.append(f"{key} : {value}")
#                         newNumber= int(i['number_of_inventory']) - int(value)
#                         i['number_of_inventory'] = newNumber
#         print(lst)
#         return lst
#                             # with open('goods.csv','r') as file2:
#                             #     reader3 = csv.DictReader(file2)
#                             #     for i in reader3:




# a=A("ofogh",65289317,8000,"titop","Cake",60,2025-5-5)
# b = A.selection_of_good(shoes= 3 ,chokolate = 3 ,candy=3)





# import csv
# def BlackList(*args):
#     lst=[]
#     with open('user.csv','r') as file:
#         reader = csv.DictReader(file)
#         for i in reader:
#             for j in args:
#                 if j in i['username'] and i['role'] == 'customer':
#                     lst.append(f"{i['username']}")
#     print(lst)                
#     return lst
# BlackList("09191049849","09191049849","09191049849")

# def edit_info(self, **kwargs):
#     allowed_keys = self.__dict__.keys() - {"store"} - {"barcode"} - {"barcode"}
#     if all(x in allowed_keys for x in kwargs.keys()):
#         self.__dict__.update((k, v) for k, v in kwargs.items())
#         return self
#     else:
#         raise ZeroDivisionError("Error! You can only change city, street, number for an address!")