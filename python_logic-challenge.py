"""
define a class called User, which recieves the first name and the year of birth
create a method called "Welcome" which should display "Welcome Name, you were born during the 20th century" or 21st if the user was born after 2000
welcome 2 users to test this out
"""


class User():
    def __init__(self, first_name, year_of_birth):
        
        self.first_name = first_name
        self.year_of_birth = year_of_birth
    
    def welcome(self):
        return f"Hello {self.first_name}, you were born during the {self.century()} century"
    
    def century(self):
        if self.year_of_birth > 2000:
            return "21st"
        else:
            return "20th"

lizzie = User("Lizzie", 1999)
print(lizzie.welcome())
gabriella = User("Gabriella", 2003)
print(gabriella.welcome())
    