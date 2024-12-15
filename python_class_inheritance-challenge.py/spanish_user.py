from user import User

class SpanishUser(User):
    def greet(self):
        print(f"Hola {self.name}")