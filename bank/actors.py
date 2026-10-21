from datetime import datetime

class Person:
    def __init__(self, firstname: str, name: str):
        self.firstname = firstname
        self.name = name

    def get_full_name(self):
        return f"{self.firstname.capitalize()} {self.name.upper()}"

    def __str__(self):
        return self.get_full_name()
        

class Client(Person):
    def __init__(self, firstname, name, date_joint: datetime):
        # fonction spéciale qui exécute la méthode de la classe parent MAIS sur l'objet courant
        super().__init__(firstname, name)
        self.date_joint = date_joint

    def get_date_joint(self, format="%Y-%m-%d"):
        return self.date_joint.strftime(format)

    def __str__(self):
        return f"{super().__str__()}, date: {self.get_date_joint()}"