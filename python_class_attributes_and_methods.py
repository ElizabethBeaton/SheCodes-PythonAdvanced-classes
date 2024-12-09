"""This is a class definition"""
class Dog:
    """This is the initialiser method"""
    def __init__(self, name, age, colour):
        """below are attributes"""
        self.name = name
        self.age = age
        self.colour = colour
        self.healthy = True 
        """you can also have a default value for an attribute inside an initialiser"""
        
    """This is a method""" 
    def say_hello(self): 
        """this^ is a method where the dog can say hello"""
        """Say hello with the dog name"""
        print(f"Hello, im a dog named {self.name}")
        print(f"I am {self.age} years old")
        print(f"My fave colour is {self.colour}")    
           
    """This is another method (get_older)"""            
    def get_older(self):
        self.age = self.age + 1
        
    """This is another method (rename)"""    
    def rename(self, new_name):
        self.name = new_name
        """in this instance, we are renaming so providing a new name"""
    """This is another method (new_fave_colour)"""    
    def new_fave_colour(self, new_colour):
        self.colour = new_colour
        
    def is_sick(self):
        self.healthy = False
    
    def is_healthy(self):
        self.healthy = True
    
"""Below, i am instantiating the class and using its methods"""

      
            
snoopy = Dog("Snoopy", 2, "green")
"""Here, i am creating an object of the Dog class. This is called instantiaion"""
snoopy.say_hello() 
snoopy.get_older()
"""Hello i am a dog names snoopy"""
"""I am 2 years old"""
snoopy.rename("Willow")
snoopy.say_hello()
"""Hello, im a dog named Willow"""
"""I am 3 years old"""
"My fave colour is green"
snoopy.new_fave_colour("pink")
snoopy.say_hello()
"""Hello, im a dog named Willow"""
"""I am 3 years old"""
"My fave colour is pink"
snoopy.is_sick()
print(snoopy.healthy)







