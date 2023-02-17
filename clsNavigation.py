from clsCommand import *
from clsSecurity import Security

class Navigation:
    def __init__(self):
        self.com = Command()
        self.sec = Security()
    
    def nav_commands(self, answer):
        if answer == "/help":
            self.com.help()

            
        elif answer == "/add":
            self.com.add()
        elif answer == "/delete":
            self.com.delete()
        elif answer == "/edit":
            self.com.edit()
        elif answer == "/search":
            self.com.search()
        else: # answer == "/view":
            self.com.view()
        
    