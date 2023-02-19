from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

from rich.console import Console


from clsSecurity import *
from clsValidInfo import *


class Command:
    def __init__(self):
        self.cls_sec = Security()
        self.paint = Console()
        self.na = NameValid
        self.su = SurnameValid
        self.ag = AgeValid
        self.ph = PhoneValid
        self.list = ["/add", "/delete", "/edit", "/search", "/view", "/help"]
        self.values = ["name", "surname", "age", "phone"]

    def help(self):
        self.cls_sec.cls()
        table = ColorTable(theme=Themes.OCEAN)
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
        self.paint.print("[blue]\nRead table and choose command[/blue]")

    def add(self): # Good
        self.cls_sec.cls()
        self.paint.print("[green]\n\tAdding new user [blue]1/4[/blue]\n[/green]")
        self.paint.print("[green]Name:[/green]")
        new_name = self.paint.input(str("[blue](add)[/blue] >>> "))
        name = self.na(new_name).valid()

        self.cls_sec.cls()
        self.paint.print("[green]\n\tAdding new user [blue]2/4[/blue]\n[/green]")
        self.paint.print("[green]Surname:[/green]")
        new_surname = self.paint.input(str("[blue](add)[/blue] >>> "))
        surname = self.su(new_surname).valid()
        
        self.cls_sec.cls()
        self.paint.print("[green]\n\tAdding new user [blue]3/4[/blue]\n[/green]")
        self.paint.print("[green]Age:[/green]")
        new_age = self.paint.input(str("[blue](add)[/blue] >>> "))
        age = self.ag(new_age).valid()

        self.cls_sec.cls()
        self.paint.print("[green]\n\tAdding new user [blue]4/4[/blue]\n[/green]")
        self.paint.print("[green]Phone:[/green]")
        new_phone = self.paint.input(str("[blue](add)[/blue] >>> "))
        phone = self.ph(new_phone).valid()

        new_user = {"name": name, "surname": surname, "age": age, "phone": phone}
        self.cls_sec.decorate_loading()
        data = self.cls_sec.bin_load()  
        self.cls_sec.bin_add(data, new_user)
        self.cls_sec.rep_add(name, surname)

        self.cls_sec.cls()
        self.paint.print(f"[green]\n\tDone! {name} {surname} added\n[/green]")

    def delete(self):
        self.cls_sec.cls()
        data = self.cls_sec.bin_load()
        if data['users'] != []:
            lst_users = []
            self.paint.print("[green]\n\tFinding user for delete\n[/green]")
            self.paint.print("[yellow]Phone:[/yellow]")
            phone = self.paint.input(str("[blue](delete)[/blue] >>> "))
            self.cls_sec.decorate_loading()

            for user in data['users']:
                for k, v in user.items():
                    if phone == v:
                        lst_users.append(user)
            self.cls_sec.cls()

            if lst_users != []:
                table = ColorTable(theme=Themes.OCEAN)
                table.field_names = ["Name", "Surname", "Age", "Phone"]
                for user in lst_users:
                    table.add_row([user['name'], user['surname'], user['age'], user['phone']])
                table.align = 'l'
                table.sortby = "Name"
                print(table)

                answer = ''
                while answer != 'Y' and answer != 'n':
                    answer = self.paint.input(str("[green]Are you sure?[/green] [blue]Y/n:[/blue] >>> "))
                if answer == 'Y':
                    for users in data['users']:
                        for user in lst_users:
                            if users['phone'] == user['phone']:
                                name = users['name']
                                surname = users['surname']
                                data['users'].pop(data["users"].index(users))
                    self.cls_sec.bin_add(data, '')
                    self.cls_sec.rep_delete(name, surname)

                    self.cls_sec.cls()
                    self.paint.print(f"[green]\n\tDeleted {name} {surname}\n[/green]")

                else:
                    self.cls_sec.cls()
                    self.paint.print("[red]\n\tDelete been cancelled\n[/red]")
            else:
                self.cls_sec.cls()
                self.paint.print("[red]\n\tUnvilible user\n[/red]")
        else:
            self.cls_sec.cls()
            self.paint.print("[red]\n\tTable empty\n[/red]")
            
    def edit(self): # Good
        self.cls_sec.cls()
        data = self.cls_sec.bin_load()
        if data['users'] != []:
            lst_users = []
            self.paint.print("[green]\n\tFinding user for edit\n[/green]")
            self.paint.print("[yellow]Phone:[/yellow]")
            phone = self.paint.input(str("[blue](edit)[/blue] >>> "))
            self.cls_sec.decorate_loading()

            for user in data['users']:
                for k, v in user.items():
                    if phone == v:
                        lst_users.append(user)
            self.cls_sec.cls()
            if lst_users != []:
                table = ColorTable(theme=Themes.OCEAN)
                table.field_names = ["Name", "Surname", "Age", "Phone"]
                for user in lst_users:
                    table.add_row([user['name'], user['surname'], user['age'], user['phone']])
                table.align = 'l'
                table.sortby = "Name"
                print(table)

                answer = ''
                categories = ''
                new_value = ''
                while answer != 'Y' and answer != 'n':
                    answer = self.paint.input(str("[green]Are you sure?[/green] [blue]Y/n:[/blue] >>> "))
                if answer == 'Y':
                    while categories != 'name' and categories != 'surname' and categories != 'age' and categories != 'phone':
                        print("| Name | Surname | Age | Phone |")
                        categories = self.paint.input(str("[yellow]Your decision:[/yellow] >>> ")).lower()
                    while new_value == '':
                        new_value = self.paint.input(str("[yellow]New value:[/yellow] >>> "))
                    
                    for users in data['users']:
                        if (users['name'] == user['name'] and users['surname'] == user['surname'] and
                            users['age'] == user['age'] and users['phone'] == user['phone']):
                            users[categories] = new_value

                            self.cls_sec.decorate_loading()
                            self.cls_sec.rep_edit(user['name'], categories, new_value)
                            self.cls_sec.bin_add(data, '')
                            self.cls_sec.cls()
                            self.paint.print(f"[green]\nDone! {user['name']} change {categories} > {new_value}\t\n[/green]")

                else:
                    self.cls_sec.cls()
                    self.paint.print("[green]\n\tEdit been cancelled\n[/green]")
            else:
                self.cls_sec.cls()
                self.paint.print("[red]\n\tUnvilible user\n[/red]")

        else:
            self.cls_sec.cls()
            self.paint.print("[red]\n\tTable empty\n[/red]")
                    
    def search(self): # Good
        self.cls_sec.cls()
        data = self.cls_sec.bin_load()
        if data['users'] != []:
            lst_users = []
            self.paint.print("[green]\n\tFind user of search\n[/green]")
            self.paint.print("[blue]Anythiks:[/blue]")
            value = input(str(">>> "))
            self.cls_sec.decorate_loading()
            for user in data['users']:
                for k, v in user.items():
                    if value in v:
                        lst_users.append(user)
            if lst_users != []:
                self.cls_sec.cls()
                self.paint.print(f"[green]\n\tСпівпадіння [blue]{value}[/blue] є тут\n[/green]")
                table = ColorTable(theme=Themes.OCEAN)
                table.field_names = ["Name", "Surname", "Age", "Phone"]
                for user in lst_users:
                    table.add_row([user['name'], user['surname'], user['age'], user['phone']])
                table.align = 'l'
                table.sortby = "Name"
                print(table)

                pause = input()
                self.cls_sec.cls()
                self.paint.print("[green]\n\tHixto ne hide\n[/green]")
            else:
                self.cls_sec.cls()
                self.paint.print("[red]\n\tUnvilible user\n[/red]")
        else:
            self.cls_sec.cls()
            self.paint.print("[red]\n\tTable empty\n[/red]")
        
    def view(self): # Good
        data = self.cls_sec.bin_load()
        self.cls_sec.cls()
        self.paint.print("[green]\n\tLoading...\n[/green]")
        self.cls_sec.decorate_loading()
        self.cls_sec.cls()

        if data['users'] != []:
            self.cls_sec.cls()
            self.paint.print("[green]\n\tTable opened\n[/green]")
            table = ColorTable(theme=Themes.OCEAN)
            table.field_names = ["Name", "Surname", "Age", "Phone"]
            for user in data['users']:
                table.add_row([user['name'], user['surname'],user['age'], user['phone']])
            table.align = 'l'
            table.sortby = "Name"
            print(table)

            pause = input()
            self.cls_sec.rep_view()
            self.cls_sec.cls()
            self.paint.print("[red]\n\tTable closed\n[/red]")
        else:
            self.cls_sec.cls()
            self.paint.print("[red]\n\tTable empty\n[/red]")