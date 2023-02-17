import pickle
import os
from tqdm import tqdm
from time import sleep
from os import system
from prettytable import PrettyTable
from datetime import datetime as dt


class Security:
    def __init__(self):
        self.date_now = f"[{dt.strftime(dt.now(), 'Day: %d.%m.%y | Time: %H:%M:%S')}]"
        self.FILE_BIN = "data.bin"
        self.FILE_TXT = 'report.txt'

    # Start
    def cls(self):
        # from os import system
        system("cls")

    def shutdown(self):
        # from os import system
        system("shutdown /s /t 5")

    def install_pickle(self):
        # import pickle
        system("pip install pickle")

    def install_prettytable(self):
        # from prettytable import PrettyTable
        system("pip install prettytable")

    def install_tqdm(self):
        from tqdm import tqdm
        system("pip install tqdm")
    
    def decorate_loading(self):
        for i in tqdm(range(100),
            desc= "Loading users...",
            unit = " users",
            ncols = 100,
            mininterval = 0.05): 
            sleep(0.05)
    # Start #

    # Report in security
    def login(self):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Fixed log in\n")
    
    def txt_new_create(self):
        with open(self.FILE_TXT, 'w') as file:
            file.write(f"{self.date_now} Create a new file\n")
            file.write(f"{self.date_now} Fixed log in\n")
            
    def bin_new_create(self):    
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Create a new bin\n")
    
    def user_added(self, name, surname):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Added {name} {surname}\n")

    def user_deleted(self):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Deleted user\n")
    
    def users_view_report(self):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Users follow\n")

    def user_edit_report(self, user):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Edit {user['name']} {user['surname']}\n")
    # Report in security #

    # Work with file bin
    def bin_load(self):
        if os.path.isfile(self.FILE_BIN) == True:
            with open(self.FILE_BIN, 'rb') as file:
                data = pickle.load(file)
            return data  
        else:
            return []

    def bin_dump(self, record: dict): # add new user
        with open(self.FILE_BIN, 'wb') as file:
            if record == '':
                pickle.dump(data, file)
            else:
                data = {"user":[record]}
                pickle.dump(data, file)

    def bin_add(self, data, record: list): # create new bin
        with open(self.FILE_BIN, 'wb') as file:
            if record == '':
                pickle.dump(data, file)
            else:
                data["user"].append(record)
                pickle.dump(data, file)
    # Work with file bin #

    def user_find(self, phone):
        try:
            data = self.bin_load()
        except:
            print("File is clean")
        else:
            if data != []:
                self.decorate_loading()
                for user in data["user"]:
                    if user['phone'] == phone:
                        return user
            else:
                return "None"
    
    def user_delete(self, user):
        data = self.bin_load()
        self.decorate_loading()
        for users in data["user"]:
            if (users['name'] == user['name'] or
                    users['surname'] == user['surname'] or
                    users['age'] == user['age'] or
                    users['phone'] == user['phone']):
                data["user"].pop(data["user"].index(users))
                self.bin_add(data, record = '')
                self.cls()
                
    def user_dump(self, user: list):
        self.decorate_loading()
        record = {"name": user[0], "surname": user[1],
            "age": user[2], "phone": user[3]}
        try:
            data = self.bin_load()  
        except:
            self.bin_dump(record)
            self.bin_new_create()
        else:
            self.bin_add(data, record)

    def user_edit(self, user, value, new):
        data = self.bin_load()
        for users in data['user']:
            if (users['name'] == user['name'] or
                users['surname'] == user['surname'] or
                users['age'] == user['age'] or
                users['phone'] == user['phone']):
                users[value] = new
                self.bin_add(data, record='')
            else:
                pass

    def user_anything(self, value):
        data = self.bin_load()
        if data == []:
            return []
        list_users = []
        for users in data['user']:
            for k, v in users.items():
                if value in v:
                    list_users.append(users)
        return list_users

    def table_for_search(self, users, field_names, add_row):
        for user in users:
            print(user)
            self.cls()
            table = PrettyTable()
            table.field_names = field_names
            for user in users:
                table.add_row(add_row)
            table.align = 'l'
            print(table)