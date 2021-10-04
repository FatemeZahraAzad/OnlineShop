import logging

import HandleFile

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='a',
                    format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")


class products:
    idfc = HandleFile.handleFile('goods.csv')
    file = HandleFile.handleFile('purchase_invoice.csv')

    def __init__(self, store, barcode, price, brand, product_name, number_of_inventory,
                 expiration_date):  # بارکد,قیمت,برند,نام کالا,تعداد موجودی,تاریخ انقضا
        self.store = store
        self.barcode = barcode
        self.price = price
        self.brand = brand
        self.product_name = product_name
        self.number_of_inventory = number_of_inventory
        self.expiration_date = expiration_date

    def saving(self):
        self.idfc.append_info_user(self.__dict__)