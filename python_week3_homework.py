"""
Display 2 subplots next to each other
The first one should display the temperature deviation using a linear plot.
The second one should display the CO2 deviation using a bar chart
Save the result inside an image
Make the plots look nice and readable
"""

# create subplots
# create first subplot with °C deviation
# create second subplot with the co2 emissions
# improve everything and sav in png file



import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1)

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

ax1.plot(years, temp_anomalies, marker="o", alpha=0.5, linestyle="--")
ax1.set_title("Global Temperature Anomalies")
ax1.set_ylabel("Temperature Anomaly (in °C)")
ax1.set_xlabel("Year")
ax1.grid(True)
ax1.set_xticks(years)

ax2.bar(years, co2_emissions, color='g', alpha=0.5)
ax2.set_title("Global CO2 Emissions")
ax2.set_ylabel("Emissions (billions of metric tons)")
ax2.set_xlabel("Year")
ax2.grid(True)

plt.tight_layout()
plt.savefig("fig1-week3hw.png")
plt.show()