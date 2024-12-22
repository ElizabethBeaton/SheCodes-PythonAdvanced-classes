"""
Ideally, it will print out 
it is 24 in lisbon
it is 30 in paris
no city data found
it is 23 in new york
    """
import csv 

with open('cities.csv', 'r') as city_file:
    csv_reader = csv.reader(city_file)
    
    for cities in csv_reader:
        if len(cities) > 0:
            print(f"It is {cities[1]} in {cities[0]}")  

    """
    can do this, it would work
    """

"""
using except handling:
"""

with open('cities.csv', 'r') as city_file:
    csv_reader = csv.reader(city_file)
    
    for cities in csv_reader:
        try:
            print(f"It is {cities[1]} in {cities[0]}") 
        except IndexError:
            print("no city data found")



