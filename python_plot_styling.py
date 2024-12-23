"""
https://matplotlib.org/
"""

import matplotlib.pyplot as plt

years = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030]
paris_population = [11, 9, 9.5, 12, 11.5, 12, 12, 11.5]
new_york_population = [9, 8, 11.5, 13, 15, 14, 16, 18.5]
sydney_population = [7, 8, 11, 15, 12, 16, 13, 15]

plt.style.use('Solarize_Light2')

plt.plot(years, paris_population, label="Paris", color='#EC6CF9', marker=".")
plt.plot(years, new_york_population, label="New York", color='#2C0515', linewidth="7")
plt.plot(years, sydney_population, label="Sydney", color='#A43E61', linestyle="--")

plt.grid(True)

plt.title("Population growth") 
plt.xlabel("Year")
plt.ylabel("Population (in Million)")
plt.legend()

plt.show() 
