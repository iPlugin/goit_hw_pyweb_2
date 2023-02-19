from clsCommand import *
from clsSecurity import Security

class Navigation:
    def __init__(self):
        self.cls_com = Command()
        self.cls_sec = Security()
    
    def nav_commands(self, answer):
        if answer == "/help":
            self.cls_com.help()
        elif answer == "/add":
            self.cls_com.add()
        elif answer == "/delete":
            self.cls_com.delete()
        elif answer == "/edit":
            self.cls_com.edit()
        elif answer == "/search":
            self.cls_com.search()
        else: # answer == "/view":
            self.cls_com.view()