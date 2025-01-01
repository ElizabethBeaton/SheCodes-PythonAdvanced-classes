temperatures = [10, 12, 14, 15]

# Print the list
print(temperatures)

# Modify an existing temperature
temperatures[1] = 16

# Print the modified item
print(temperatures[1])


# Add a temperature to the list
# Print the the newly added item
temperatures.append(20)
print(temperatures[4])


forecast = {
  "Monday": { "temperature": 21, "condition": "Rainy"},
  "Tuesday": { "temperature": 20, "condition": "Sunny"},
  "Wednesday": { "temperature": 23, "condition": "Cloudy"},
  "Thursday": { "temperature": 24, "condition": "Sunny"},
}

# Print the dictionary
print(forecast)

# Modify Wednesdays temperature to 25 and Sunny
forecast["Wednesday"]["temperature"] = 25
forecast["Wednesday"]["condition"] = "Sunny"

# Print Wednedays temperature
print(forecast["Wednesday"]["temperature"])

# Add forecast for Friday, 27, Cloudy
forecast["Friday"] = {"temperature": 25, "condition": "Sunny"}
print(forecast)

# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy

new_friday_temperature = ("Friday's temperature will be 27 degrees and cloudy")
forecast['Friday']['temperature'] = new_friday_temperature
print(forecast)


print(f"Friday's temperature will be {forecast["Friday"]["temperature"]} degrees and {forecast["Friday"]["condition"]}")

#cleaner:
day = "Friday"
friday_temp = forecast["Friday"]["temperature"]
friday_condition = forecast["Friday"]["condition"].lower()
print(f"{day}'s temperature will be {friday_temp} degrees and {friday_condition}")
