from average_temperature_calculator import AverageTemperatureCalculator

def calculate_average_temperature_for_continent(temperatures_list, continent_name):
  """
  Calculate the average temperature for a continent

  Return the average temperate as a float
  """
  total = 0
  cities_count = 0

  for temperature in temperatures_list:
    if temperature['continent'] == continent_name:
      total = total + float(temperature['temperature'])
      cities_count = cities_count + 1

  average = total / cities_count
  rounded_average = round(average, 2)

  return rounded_average

def display_average_temperature(average): 
  """
  Print the average temperature in a formatted message
  """
  print(f"Average temperature in North America is: {average} degrees")

# Inital data
temperatures = [
  {'city': "Paris", 'continent': "Europe", "temperature": "12"},
  {'city': "Los Angeles", 'continent': "North America", "temperature": "22"},
  {'city': "Paris", 'continent': "Asia", "temperature": "18"},
  {'city': "New York", 'continent': "North America", "temperature": "14"},
  {'city': "Sao Paulo", 'continent': "South America", "temperature": "25"},
  {'city': "Toronto", 'continent': "North America", "temperature": "2"}
]

# Use a function to calculate the average
average = calculate_average_temperature_for_continent(temperatures, "North America")

# Use a class to calculate the average
# calculator = AverageTemperatureCalculator(temperatures)
# average = calculator.average("North America")

display_average_temperature(average)
