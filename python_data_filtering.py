# Converting data
population = "1000"
population_number = int(population) # converts the 1000 string into an integer
population_number = float(population) # 1000.0 (float has decimals)
population_string = str(population_number) # "1000" converting back to string

print(population_string)

# Data filtering

european_countries = ["France", "Italy", "Spain"]        #list of euro countries
populations = {                                         #dictionary of dictionaries of population data. Each key is a country, and the value is another dictionary with details including its capital and population.
    "France": { "capital": "Paris", "population": "7000000"},
    "England": { "capital": "London", "population": "5000000"}, 
    "Spain": { "capital": "Madrid", "population": "3000000"}, 
    "Germany": { "capital": "Berlin", "population": "5000000"}, 
    "USA": { "capital": "Washington", "population": "3000000"}, 
}


#how would we get the population of only European countries?
"""
could loop through the european countries list and see if any of the values is inside my populations dictionary.
if it is, we'll get the population, convert it into an integer/float.
maybe use an if else statement for float
"""

# create population count variable
total_population = 0  #initialising a total_population variable to 0. This will story the su on populations if euro countries

# loop through each country in the european countries list:
for country in european_countries:          # this will check each European country
    if country in populations:              # check if the country exists in the populations dictionary. if the country (eg "France") is in populations, proceed.
        country_population = int(populations[country]["population"])   # getting the population of the country and then changing the string value into an int. Here, we are accessing the population from the inner dictionary, which is stored as a string. We're then converting it
        total_population = total_population + country_population   # add the pupulation to total_population. Similarly could write 'total_population += country_population', which would just add on to it
# check if we can get the population
# add it to the total count
# print the total population
print(f"The European population is: {total_population}") # thisll print out the total population on the European countried in the list