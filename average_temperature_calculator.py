class AverageTemperatureCalculator:
  """
  Calculate the average temperature for a continent
  """
  def __init__(self, temperatures):
    """
    Initialize the object with a list of temperature dictionaries
    """
    self.temperatures = temperatures

  def average(self, continent):
    """
    Calculate the average temperature for a continent

    Return the average a float, rounded with 2 decimals
    """
    total = 0
    cities_count = 0

    for temperature in self.temperatures:
      if temperature['continent'] == continent:
        total = total + float(temperature['temperature'])
        cities_count = cities_count + 1

    average = total / cities_count
    rounded_average = round(average, 2)

    return rounded_average