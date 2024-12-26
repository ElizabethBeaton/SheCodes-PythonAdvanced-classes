import matplotlib.pyplot as plt

lisbon_temperatures = [25, 26, 28, 24, 22]
new_york_temperatures = [15, 17, 12, 20, 22]
sydney_temperatures = [10, 12, 11, 8, 7]

days = ['Monday', 'Tuesday', 'Wednesday', "Thursday", 'Friday']

plt.style.use('seaborn-v0_8-darkgrid')

plt.plot(days, lisbon_temperatures, label="Lisbon", marker=".")
plt.plot(days, new_york_temperatures, label="New York", linestyle="--")
plt.plot(days, sydney_temperatures, label="Sydney", color="#2C0515")


plt.legend()
plt.grid(True)
plt.xlabel("Days")
plt.ylabel("Temperatures (in celcius)")

plt.title("Weather forecast")


plt.show()
