import HandleFile
import csv
import logging


logging.basicConfig(level=logging.INFO,filename='logs.log',filemode='a',format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")

class products:

    idfc = HandleFile.handleFile('goods.csv') 
    file = HandleFile.handleFile('purchase_invoice.csv')
    
    def __init__(self,store,barcode,price,brand,product_name,number_of_inventory,expiration_date): #بارکد,قیمت,برند,نام کالا,تعداد موجودی,تاریخ انقضا
        self.store = store
        self.barcode=barcode
        self.price=price
        self.brand=brand
        self.product_name=product_name
        self.number_of_inventory = number_of_inventory
        self.expiration_date=expiration_date

    # def validation_inventory(self):
    #     lst = []
    #     with open('goods.csv', 'r') as file:
    #         reader = csv.DictReader(file)
    #         for i in reader:
    #             if int(i['number_of_inventory']) <= 10:
    #                 lst.append(f"{i['product_name']} : {i['number_of_inventory']}")
    #     print(lst)
    #     return self
    
    def show_products(self):
        lst = []
        with open('goods.csv','r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if self in i['store'] :
                    print(i)
                    if int(i['number_of_inventory']) <= 10:
                        lst.append(f"{i['product_name']} : {i['number_of_inventory']}")
                        if lst:
                            print()
        print(f"!!!WARNING!!! >> {lst}")
        return self

    def show_buy(self):
            with open('purchase_invoice.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if self in i['store']:
                        print(i)
              
    def saving(self):
        self.idfc.append_info_user(self.__dict__)

# a = products("kuroosh","52694531","98000","dark","chokolate","15","2020-11-9")
# a.saving()
# b =products("seven","123456789","4500","yumi","candy","9","2020-12-20")
# b.saving()
# c = products("Ofogh","497634215","76000","adidas","bag","1","2040-10-13")
# c.saving()
# d = products("Artesh","356942586","200000","","Rice","20","2026-5-17")
# d.saving
# d.validation_inventory()
#__________________________________________________________________________________________________________
