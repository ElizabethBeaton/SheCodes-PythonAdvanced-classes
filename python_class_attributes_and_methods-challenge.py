"""
define a class User who recieves 2 attributes in the iitialise, a first name and a last name.
create a method called full_name, which returns the user's full name
create 2 users with different names and print their full name
change the first name of the first object and print the full name again 
"""

class User:
    
    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
        
    def rename_first_object(self, new_name):
        self.first_name = new_name
        
    
lizzie = User("Lizzie", "Beaton")
gabriella = User("Gabriella", "Beaton")
lizzie.full_name()
gabriella.full_name()
lizzie.rename_first_object("Caroline")
lizzie.full_name()
