"""
Display each customer from the CSV in this format:
“Customer #53, Patricia Goodwin, vaughanchristy@lara.biz”
    """
    
import csv

with open('python_week2_homework/customers.csv', 'r') as customers_file:
    csv_reader = csv.reader(customers_file)
    
    for customers in csv_reader:
        """
    can also write:
    
    id = customers[0]
    first_name = cutomers[2]
    last_name = customers[3]
    email = customers[9]
    print(f"Customer #{id}, {first_name} {last_name}, {email}")
    
    """
        print(f"Customer #{customers[0]}, {customers[2]} {customers[3]}, {customers[9]}")