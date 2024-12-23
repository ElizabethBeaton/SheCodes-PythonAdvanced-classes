import matplotlib.pyplot as plt

"""
index = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(index)
plt.plot(squares)

plt.title("This is my first chart")

plt.legend(["Linear values", "Square values"])
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
"""

years = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030]
paris_population = [8, 9, 10, 11, 11.5, 12, 12, 11.5]
new_york_population = [6, 8, 11, 13, 15, 14, 16, 18.5]

plt.plot(years, paris_population)
plt.plot(years, new_york_population)

plt.title("Population growth") #title of graph
plt.xlabel("Year")
plt.ylabel("Population (in Million)")
plt.legend(["Paris", "New York"]) #key

plt.show() #need this to display graph


