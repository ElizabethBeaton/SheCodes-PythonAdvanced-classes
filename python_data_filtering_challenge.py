#list of dictionaries
temperatures = [
  {'city': "Paris", 'continent': "Europe", "temperature": "12"},
  {'city': "Los Angeles", 'continent': "North America", "temperature": "22"},
  {'city': "Paris", 'continent': "Asia", "temperature": "18"},
  {'city': "New York", 'continent': "North America", "temperature": "14"},
  {'city': "Sao Paulo", 'continent': "South America", "temperature": "25"},
  {'city': "Toronto", 'continent': "North America", "temperature": "2"}
]
# CHALLENGE:
# Given the list of temperatures, calculate and print the average temperature of north American cities

# loop through the dictionary, get access to the temperatures of the north american cities
# use an if statement - if the continent is north america then get access to the temp
# already have made a variable to cal the average temp so i can add the north american temps to this
# rememeber to change the temp from a str to int

total_temperature = 0
north_american_cities = 0 #this is needed as we will be dividing this

for temperature in temperatures: # look through all of the temperatures
    if temperature['continent'] == "North America":
        total_temperature = total_temperature + float(temperature["temperature"]) #goal is to filter to see all north american cities. for now we will look through all the cities. total_temp starts at 0, so just adding on the rest
        north_american_cities = north_american_cities + 1
    
average_temperature = total_temperature / north_american_cities #making the average temperature the total of the total temp divided by the north american cities temp

print(f"The average temperature of North American cities is: {round(average_temperature, 2)} degrees") # 12.67  using round function to round of 2 decimal places

