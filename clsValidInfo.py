class clsValidInfo:
    def valid(self):
        raise NotImplementedError

class NameValid(clsValidInfo):
    def __init__(self, name):
        self.name = name
    
    def valid(self):
        return f"{self.name}".title().strip()

class SurnameValid(clsValidInfo):
    def __init__(self, surname):
        self.surname = surname

    def valid(self):
        return f"{self.surname}".title().strip()

class AgeValid(clsValidInfo):
    def __init__(self, age):
        self.age = age

    def valid(self):
        return f"{self.age}".strip()

class PhoneValid(clsValidInfo):
    def __init__(self, phone):
        self.phone = phone

    def valid(self):
        return f"{self.phone}".strip()
    



