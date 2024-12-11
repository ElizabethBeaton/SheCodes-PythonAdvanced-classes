"""
define a class People who recieves 4 attributes in the initialiser, a first name, last name, age, fave animal.
create a method called full_name, which returns the user's full name
create a method called sentence, then form a sentence with all the attributes
create a method to increment the age of the individual
create 3 users with different names and print their full name
make a change to one of the attributes.
"""

class People:
    
    def __init__(self, first_name, last_name, age, fave_animal):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fave_animal = fave_animal
    
        
    def full_name(self):
        print(f"My name is {self.first_name} and my last name is {self.last_name}")
        
    def sentence(self):
        print(f"My full name is {self.first_name} {self.last_name}, I am {self.age} years old and my favourite animal is a {self.fave_animal}")
    
    def birthday(self):
        self.age = self.age + 1
        print(f"I am now {self.age} years old and I feel cooler than I did last year")
    
    def rename(self, new_name):
        self.first_name = new_name    
        
    
    
jack = People("Jack", "Beaton", 11, "Dog")
jack.full_name() 
james = People("James", "Beaton", 22, "Lion")
michael = People("Michael", "Beaton", 33, "Tiger")
james.sentence()
michael.birthday()
jack.birthday()
james.rename("Denis")
james.sentence()

