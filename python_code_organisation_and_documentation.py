def calculate_average_temperure_for_continent(temperatures_list, continent_name):
    total = 0
    cities_count = 0 

    for temperature in temperatures_list: 
        if temperature['continent'] == continent_name:
            total = total + float(temperature["temperature"])
            cities_count = cities_count + 1
    
    average = total / cities_count

    return round(average, 2)

def display_average_temperature(average):
    print(f"The average temperature of North American cities is: {average} degrees") 

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

average = calculate_average_temperure_for_continent(temperatures, "North America")

display_average_temperature(average)



