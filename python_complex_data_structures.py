"""
diff with list and dictionary:
lists = []
dictionary = {}
list is similar to an array and a very simply basic data structure. 
each item will only have one value
dictionary is a more sophisticated way to organise your data
eg:
"""

cities = ["Lisbon", "Paris", "London", "Sydney"]
print(len(cities))
cities[0] #Lisbon
cities[2] #London

cities = [
    ["Lisbon", "Porto"], 
    ["Paris", "Marseille", "Lyon"], 
    ["New york", "Miami", ["San Francisco", "Los Angeles"]]
]
american_cities = cities[2] #getting access to the [2] of the list (us cities)
print(american_cities[2][1]) # getting access to the second index in this particular list
#would print Los Angeles


print(american_cities[2][0]) #this would print San Francisco
californian_cities = american_cities[2] #speciying the list inside the list so easier to access
print(californian_cities[1])

#DICTIONARIES
"""
with lists we use index values, with dictionaries we use keys.
below is a simple dictionary
"""

cities = {
    "Portugal": "Lisbon",
    "France": "Paris",
    "USA": "New York"
}

print(cities["USA"]) # New York           (string)
country = "Portugal"                    # (variable)
print(cities[country])
#We can access it from a string, and also from a variable!

#List of dictionaries
countries = [
    {"country": "England", "city": "London"},
    {"country": "USA", "city": "Miami"},
    {"country": "Japan", "city": "Tokyo"},
]

print(countries[1]["city"])

for country in countries:
    print(country["city"]) #London, Miami, Tokyo
    print(country["country"]) #it wont always print this out in the same order as its written in. This is bcos a dictionary is not always ordered in the same order

#Dictionary of dictionaries

cities = {
    "Lisbon": { "country": "Portugal", "population": 10000 },
    "Los Angeles": { "country": "USA", "population": 20000},
    "London": { "country": "England", "population": 15000}
}

print(cities["Lisbon"]["population"]) #10000
print(cities["London"]["country"]) #England

#Dictionary operations
#Adding / modifying elements
cities = {
    "Portugal": "Lisbon",
    "France": "Paris",
    "USA": "New York"
}

#Updating a dictionary
print(cities['France']) #would print Paris
cities['France'] = "Lyon"
print(cities['France']) #replacing Paris with Lyon

#Adding a new value to a dictionary
cities['Germany'] = "Munich" #adding Germany and Munich to the list
print(cities)

print(cities.keys())
print(cities["Germany"])




#List operations
#Adding / modifying elements
cities = [
    "Lisbon", "Paris", "New York"
]

#Updating a list
cities[1] = "Lyon"
print(cities[1]) #Lyon

#Adding a new value to a list
cities.append("Munich")
print(cities[3]) #Munich
cities.remove('Munich')











