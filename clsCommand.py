from prettytable import PrettyTable
from clsSecurity import *
from clsValidInfo import *
# from rich.console import Console

class Command:
    def __init__(self):
        self.sec = Security()
        # self.cons = Console()
        self.list = ["/add", "/delete", "/edit", "/search", "/view", "/help"]
        self.values = ["name", "surname", "age", "phone"]
        self.n = NameValid
        self.s = SurnameValid
        self.a = AgeValid
        self.p = PhoneValid

    def help(self):
        self.sec.cls()
        table = PrettyTable()
        table.field_names = ["Command", "Explanation"]
        table.add_rows([
                ["/add", "- add new user"],
                ["/delete", "- delete user"],
                ["/edit", "- edit user"],
                ["/search", "- search user"],
                ["/view", "- print users"],
                ["/exit", "- exit"],
                ["/help", "- need help"]
            ])
        table.align = "l"
        table.sortby = "Command"
        print(table)
        print("Read table and choose command")

    def add(self):
        self.sec.cls()
        print("\n\tAdding new user 1/4\n")
        print("Name:")
        new_name = input(str("(add)>>> "))
        name = self.n(new_name).valid()

        self.sec.cls()
        print("\n\tAdding new user 2/4\n")
        print("Surname:")
        new_surname = input(str("(add)>>> "))
        surname = self.s(new_surname).valid()
        
        self.sec.cls()
        print("\n\tAdding new user 3/4\n")
        print("Age:")
        new_age = input(str("(add)>>> "))
        age = self.a(new_age).valid()

        self.sec.cls()
        print("\n\tAdding new user 4/4\n")
        print("Phone:")
        new_phone = input(str("(add)>>> "))
        phone = self.p(new_phone).valid()

        new_user = [name, surname, age, phone]
        self.sec.user_dump(new_user)
        self.sec.user_added(name, surname)
        self.sec.cls()
        print(f"\n\tDone! {name} {surname} added\n")

    def delete(self):
        button = True
        while button:
            self.sec.cls()
            print("\n\tFinding user for delete\n")
            print("Phone:")
            phone = input(str("(delete)>>> "))
            user = self.sec.user_find(phone)
            if user == "None":
                self.sec.cls()
                print("\n\tUnavailable user\n")
                break
            else:
                self.sec.cls()
                table = PrettyTable()
                table.field_names = ["Name", "Surname", "Age", "Phone"]
                table.add_row([user["name"], user["surname"], user["age"], user["phone"]])
                table.align = 'l'
                print(table)

                answer = ''
                while answer != "y" and answer != "N":
                    print("Are you sure? (y/N)")
                    answer = input(str(">>> "))
                    if answer == "y":
                        self.sec.user_delete(user)
                        button = False
                        print("\n\tUser deleted\n")
                        break
                    else:
                        self.sec.cls()
                        button = False
                        print("\n\tDelete been cancelled\n")
                        break
            
    def edit(self):
        button = True
        while button:
            self.sec.cls()
            print("\n\tFinding user for edit\n")
            print("Phone:")
            phone = input(str(">>> "))
            user = self.sec.user_find(phone)
            if user == "None":
                self.sec.cls()
                print("\n\tUnavailable user\n")
                break
            else:
                self.sec.cls()
                table = PrettyTable()
                table.field_names = ["Name", "Surname", "Age", "Phone"]
                table.add_row([user["name"], user["surname"], user["age"], user["phone"]])
                table.align = 'l'
                print(table)

                answer = ''
                value = ''
                while answer != "y" and answer != "N":
                    print("Are you sure? (y/N)")
                    answer = input(str(">>> "))
                    if answer == 'y':
                        while value != "name" and value != "surname" and value != "age" and value != "phone":
                            print("| Name / Surname / Age / Phone |")
                            value = input(str(">>> ")).lower()
                        print(f"Old value: {user[value]}")
                        new = input(str("New value: "))
                        self.sec.user_edit(user, value, new)
                        self.sec.user_edit_report(user)
                        self.sec.cls()
                        print("\n\tUser Edited\n")
                        button = False
                    else:
                        self.sec.cls()
                        button = False
                        print("\n\tEdit been cancelled\n")
                        break
                    
    def search(self):
        while True:
            self.sec.cls()
            print("\n\tFinding user for search\n")
            print("Anything:")
            value = input(str(">>> "))
            if value == '':
                self.sec.cls()
                print("\n\tUnavailable user\n")
                break
            users = self.sec.user_anything(value)
            if users == []:
                self.sec.cls()
                print("\n\tUnavailable user\n")
                break
            else:
               
                field_names = ["Name", "Surname", "Age", "Phone"]
                add_row = [field_names[0].lower, field_names[1].lower(), field_names[2].lower(), field_names[3].lower()]
                self.sec.table_for_search(users, field_names, add_row)

                pause = input()
                self.sec.cls()
                print("\n\tYou can't hide :)\n")
                break

    def view(self):
        data = self.sec.bin_load()
        if data != []:
            table = PrettyTable()
            table.field_names = ["Name", "Surname", "Age", "Phone"]
            for user in data['user']:
                table.add_row([user["name"], user["surname"], user["age"], user["phone"]])
            table.align = 'l'
            self.sec.cls()
            print("\n\tTable opened\n")
            self.sec.users_view_report()
            print(table)
            pause = input()
            self.sec.cls()
            print("\n\tTable closed\n")
        else:
            self.sec.cls()
            print("\n\tTable empty\n")