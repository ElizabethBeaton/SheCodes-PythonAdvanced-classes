import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1,2)

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]

ax1.plot(condition, days)
ax2.plot(condition, days)


ax1.pie(days, labels=condition)
ax1.set_title('Weather in Lisbon')
ax1.legend(days)
ax2.pie(days, labels=condition)
ax2.set_title('Weather in Lisbon')
ax2.legend(days)



plt.tight_layout()
plt.savefig("piechart_output.png")
plt.show()
