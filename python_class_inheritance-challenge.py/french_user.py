from user import User

class FrenchUser(User):
    def greet(self):
        print(f"Bonjour {self.name}")