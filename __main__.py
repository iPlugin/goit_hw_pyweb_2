import os
from clsNavigation import Navigation
from rich.console import Console

if __name__ == "__main__":
    nav = Navigation()
    cons = Console()
    # Constant
    SECUTITY = nav.sec.FILE_TXT

    # Settings imports
    nav.sec.install_pickle() 
    nav.sec.install_prettytable()
    nav.sec.install_tqdm()
    nav.sec.cls()

    # Report in security
    if os.path.isfile(SECUTITY) == True:
        nav.sec.login()
    else:
        nav.sec.txt_new_create()


    cons.print(f"""
    [blue]{chr(936)} Welcome in iPlugin {chr(169)}[/blue]
    If you need help write [green]/help[/green]
    If you wanna log out [green]/exit[/green]
    """)
    
    while True:
        answer = input(str("(main)>>> ")).lower().strip()
        if answer == "/exit":
            nav.sec.cls()
            cons.print("""
    [blue]iPlugin wish you:[/blue]
    [green]"Have a nice day"[/green]
    [red]Sorry but you chose
    this path yourself![/red]
    """)
            nav.sec.shutdown() 
            break
        elif answer in nav.com.list:
            nav.nav_commands(answer)
        else:
            nav.sec.cls()
            cons.print(f"""
    [blue]iPlugin announcement[/blue]
    -- [red]"{answer}" wrong command[/red] --
    If you need help write [green]/help[/green]
    If you wanna log out [green]/exit[/green]
    """)



# from clsNavigation import Navigation
# if __name__ == "__main__":
#     nav = Navigation()
#     nav.com.edit()



# # # from clsNavigation import Navigation
# # # if __name__ == "__main__":
# # #     nav = Navigation()
# # #     nav.com.search()