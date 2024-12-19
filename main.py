import csv 
#another more sophisticated way of doing this is using pandas

#open cvs file
#iterate over each row and display each row

with open('python_csv_file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    for city in csv_reader:
        print("-----")
        print(f"Country: {city[1]}")
        print(f"Capital city: {city[0]}")
        print(f"Currency: {city[2]}")
        
    """
    this would print out the following lists inside an array: 
    ['Lisbon', 'Portugal', 'Euros'] 
['Paris', 'Fraance', 'Euros']
['Tokyo', 'Japan', 'Yen']

so now we can manipulate.
    """
    
"""
how to loop through a csv file in python and have this in a clear manner so we can do some sort of manipulation
"""