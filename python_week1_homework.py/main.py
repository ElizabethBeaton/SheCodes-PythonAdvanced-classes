"""
- Create a new Weather Class
- Create a method called set_weather that sets the weather temperature and condition
- Create a method called display_weather(), which will display the weather information of a class object
- Test it with some fake data such as Paris, 27, sunny
"""

from weather import Weather

paris_weather = Weather("Paris")
paris_weather.set_weather(27, "Sunny")
paris_weather.display_weather()

lisbon_weather = Weather("Lisbon")
lisbon_weather.set_weather(44, "Great")
lisbon_weather.display_weather()

