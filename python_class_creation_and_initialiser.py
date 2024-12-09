"""classes are always capitalised. if 2+ works, camel case eg CapitalCity. """

class Dog:
    #A class defining a dog
    
    def __init__(self):
        """everytime we use init, it should have self as an argument. Everytime we use a class, we will have this
        Initialises a dog"""
        print("A new dog is now created")
        
snoopy = Dog()
milo = Dog()

"""
challenge:
define a class User which prints "Hello from the User class" when its initialising
create 3 instances of that class and store them in diff varibles
"""

class User():
    
    def __init__(self):
        print("Hello from the User class")

one = User()
two = User()
three = User()