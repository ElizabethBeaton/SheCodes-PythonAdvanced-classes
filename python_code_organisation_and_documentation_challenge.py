#fork the repl and re-organise it and add some documentation

import csv

def display_customer(customer):
    """
    Extract the data from the customer and display it
    """
    customer_id = customer[0]
    first_name = customer[2]
    last_name = customer[3]
    email = customer[9]
    
    print(f"Customer #{customer_id}, {first_name} {last_name}, {email}") #output
  


"""
Loop through eah line from the customer file
Display each customer's id, first name, last name and email
"""
with open('customers_file.csv', 'r') as customer_file:
  customers = csv.reader(customer_file) 

  for customer in customers: 
    display_customer(customer)

    

    
  