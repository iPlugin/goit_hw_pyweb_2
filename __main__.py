import os
from os import system

# About author #
AUTHOR = "iPlugin"
PHONE = '+380989229777'
# # About author # #

# constant #
FILE_IMR = 'requirements.txt'
FILE_BIN = "data.bin"
FILE_TXT = 'report.txt'
# # constant # #

# Settings imports #
packages = system(f"pip freeze > {FILE_IMR}")
packets = ['pickle', 'prettytable', 'tqdm', 'rich']
with open(FILE_IMR, 'r') as f:
    file = f.read()

for value in packets:
    if value not in file:
        system(f"pip install {value}")
# # Settings imports # #

from clsNavigation import Navigation
from rich.console import Console
import pickle


if __name__ == "__main__":
    cls_nav = Navigation()
    paint = Console()

    # Report in security #
    if os.path.isfile(FILE_TXT) == True:
        cls_nav.cls_sec.rep_login()
    else:
        cls_nav.cls_sec.rep_login_new()
    # # Report in security # #

    # Create bin file #
    if os.path.isfile(FILE_BIN) == False:
        cls_nav.cls_sec.rep_bin_new()
        with open(FILE_BIN, 'wb') as file:
            record = {'name': 'Author', 'surname': AUTHOR,
                        'age': '20', "phone": PHONE}
            data = {'users': [record]}
            pickle.dump(data, file)
    else:
        pass
    # # Create bin file # #

    cls_nav.cls_sec.cls()
    paint.print(f"""
    [blue]{chr(936)} Welcome in iPlugin {chr(169)}[/blue]
    If you need help write [green]/help[/green]
    If you wanna log out [green]/exit[/green]
    """)
    
    while True:
        answer = paint.input(str("[blue](main)[/blue] >>> ")).lower().strip()
        if answer == "/exit":
            cls_nav.cls_sec.cls()
            paint.print("""
    [blue]iPlugin wish you:[/blue]
    [green]"Have a nice day"[/green]
    [red]Sorry but you chose
    this path yourself![/red]
    """)
            cls_nav.cls_sec.shutdown() 
            break
        elif answer in cls_nav.cls_com.list:
            cls_nav.nav_commands(answer)
        else:
            cls_nav.cls_sec.cls()
            paint.print(f"""
    [blue]iPlugin announcement[/blue]
    -- [red]"{answer}" wrong command[/red] --
    If you need help write [green]/help[/green]
    If you wanna log out [green]/exit[/green]
    """)