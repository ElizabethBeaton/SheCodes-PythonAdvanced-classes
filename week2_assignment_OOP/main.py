import csv
from customer import Customer
"""above, need to import the Customer Class from the customer file
    """

with open('week2_assignment_OOP/customers.csv', 'r') as customers_file:
    customers = csv.reader(customers_file)
    
    for customer in customers:
        customer_object = Customer(customer[0], customer[2], customer[3], customer[9])
        print(customer_object.description())
        