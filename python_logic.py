"""
CLASS LOGIC
inside a class you can have any python code you want
"""

class Dog:
    """define a dog"""
    def __init__(self, name, age = 0):
        """initialise dog with name and age"""
        
        self.name = name
        self.age = age
        
    def greet(self):
        """return a dog greeting"""
        return f"Hello, I'm a {self.casual_name()} named {self.name}"
    """(casual_name() has parenthesis because its a method)"""
        
    def casual_name(self):    
        if self.age < 2:
            return "puppy"
        elif self.age < 10: 
            return "grown up dog"
        else:
            return "old dog" 
    
    
    
lily = Dog("Lily", )
print(lily.greet())