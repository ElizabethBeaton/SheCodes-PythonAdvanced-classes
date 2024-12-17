#open files
file = open('cities.txt', 'r')
cities = file.readlines()

#print content
print(cities)

for city in cities: 
   print(f"I want to visit {city.strip()}")

#OR
#more pythony approach
with open('cities.txt', 'r') as file:
    lines = file.readlines()

#loop through all the cities
for city in cities:
    print(city.strip())
    
#close the file
file.close()






with open('python2_data/countries.txt', 'r') as file:
    countries = file.readlines()

for country in countries:
    print(f"I want to go to {country.strip()}")
    
    
    
    
    """
    Takeaways:
    if file outside folder, write it siilar to example 1. 
    if inside folder eg above, would eb written as so: python2_data/countries.
    (first example would not work now as it is inside the file. would need to be 'data/cities'.)
    """
    """
    four types of handling: 
    r - read. default value. opens a file for reading. error if file does not exist
    a - append. opens a file for appending. creates a file if it des not exist
    w - write. opens a file for writing. creates a file if it does not exist
    x - create. creates a specifies file. returns an error if fle already exists
    """