import csv
from User import customer
import logging
import HandleFile
logging.basicConfig(level=logging.INFO,filename='logs.log',filemode='a',format=" %(asctime)s — %(name)s — %(levelname)s — %(message)s \n")

class Search:
    file = HandleFile.handleFile('goods.csv')
    def search_manager (type) :
        try:
            with open('purchase_invoice.csv','r') as file:   # r+
                reader = csv.DictReader(file)
                for i in reader:
                    if type == f"{i['customerName']} {i['date']}":
                        print(i)
                else:
                    print("Not found it")
        except Exception as e:
            print(e)
            logging.error("Unsuccessful search")

    def search_customer(type2):
        try:
            with open('user.csv','r') as file:   # r+
                reader = csv.DictReader(file)
                for i in reader:
                    if i['role'] == 'manager':
                        if type2 in i['store_name'] and i["Login_time"] < customer.now_time < i["Exit_time"]:
                            print(f"{i['store_name']}")
                            return type2
                else:
                    print("Not found it")
        except Exception as e:
            print(e)
            logging.error("Unsuccessful search")