import HandleFile
import csv
from hashlib import sha256
class customer:
    idfc = HandleFile.handleFile('user.csv')
    def __init__(self,role,username,password):
        self.role = role
        self.username=self.validation_name(username)
        self.password=self.validation_pasword(password)
        

    def validation_pasword(self,password):
        if password.isalnum() and len(password) >= 8:
            repeat_password = input("Repeat your password :")
            while repeat_password != password:
                repeat_password = input("Input is incorrect\nRepeat your password again :")
            return sha256(str(repeat_password).encode()).hexdigest()    
        else:
            print("invalid password")
    def validation_name(self,name):
        if name.startswith("09") and name.isdigit() and len(name) == 11 :
            with open('user.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name not in i['username']:
                        return name
                    else:
                        print("Duplicate name")
                else:
                    return name
        else:
            print("invalid username")

    def saving (self):
        self.idfc.append_info_user(self.__dict__)

        
class Manager(customer):
    idfc = HandleFile.handleFile('user.csv')
    def __init__(self, role, username, password,store_name,Login_time,Exit_time,black_list=None):
        super().__init__(role, username, password)
        self.store_name=store_name
        self.Login_time=Login_time
        self.Exit_time = Exit_time
        self.blacklist = black_list
    def saving (self):
        self.idfc.append_info_user(self.__dict__)
    
    def show(self):
        with open('user.csv','r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                if i['role'] == 'customer': 
                    print(i['username'])

    def BlackList(*args):
        lst=[]
        with open('user.csv','r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                for j in args:
                    if j in i['username'] and i['role'] == 'customer':
                        lst.append(f"{i['username']}")
        print(lst)                
        return lst


# a = customer("customer","09126853858","091910aaa")
# a.saving()

# b= Manager.BlackList("09191049849","09191049849","09191049849")
# a = Manager("manager","09191049849","091910aaa","ofogh","2018-2020",b)
# a.saving()