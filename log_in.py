import csv
class customer:
    def __init__(self,role,username,password):
        self.username=self.validation_name(username)
        self.password=self.validation_pasword(password)
        self.role = role

    def validation_pasword(self,password):
        if password.isalnum() and len(password) >= 8:
             with open('user.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if password in i['password']:
                        return password
                    else:
                        print("incorrect password")
        else:
            print("invalid password")
    def validation_name(self,name):
        if name.isdigit() and len(name) == 11 :
            with open('user.csv','r') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if name in i['username']:
                        return name
                    else:
                        print("Duplicate name")
                else:
                    return name
        else:
            print("invalid username")
            
class manager(customer):
    def __init__(self, role, username, password):
        super().__init__(role, username, password)
        