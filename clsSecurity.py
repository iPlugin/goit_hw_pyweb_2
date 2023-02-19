import pickle
from tqdm import tqdm
from time import sleep
from os import system
from datetime import datetime as dt


class Security:
    def __init__(self):
        self.date_now = f"[{dt.strftime(dt.now(), 'Day: %d.%m.%y | Time: %H:%M:%S')}]"
        self.FILE_BIN = "data.bin"
        self.FILE_TXT = 'report.txt'

    def cls(self):
        # from os import system
        system("cls")

    def shutdown(self):
        # from os import system
        system("shutdown /s /t 5")
    
    # Work with file bin #
    def bin_load(self):
        with open(self.FILE_BIN, 'rb') as file:
            data = pickle.load(file)
        return data  

    def bin_add(self, data, record: dict|str):
        with open(self.FILE_BIN, 'wb') as file:
            if record == '': # when update data
                pickle.dump(data, file)
            else: # when add new user
                data["users"].append(record)
                pickle.dump(data, file)
    # # Work with file bin # #
    
    # Report in security #
    def rep_login(self):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Fixed log in\n")
    
    def rep_login_new(self):
        with open(self.FILE_TXT, 'w') as file:
            file.write(f"{self.date_now} Create a new file\n")
            file.write(f"{self.date_now} Fixed log in\n")
            
    def rep_bin_new(self):    
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Create a new bin\n")
    
    def rep_add(self, name, surname):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Added {name} {surname}\n")

    def rep_delete(self, name, surname):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Deleted {name} {surname}\n")
    
    def rep_view(self):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Users follow\n")

    def rep_edit(self, name, change1, change2):
        with open(self.FILE_TXT, 'a') as file:
            file.write(f"{self.date_now} Edit {name} change {change1} > {change2}\n")
    # # Report in security # #

    # Decorate #
    def decorate_loading(self):
        for i in tqdm(range(100),
            desc= "Loading users...",
            unit = " users",
            ncols = 100,
            mininterval = 0.05): 
            sleep(0.05)
    # # Decorate # #