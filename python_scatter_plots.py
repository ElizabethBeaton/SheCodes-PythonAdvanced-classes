import matplotlib.pyplot as plt

x = [2, 5, 3, 9, 10]
y = [200, 100, 300, 100, 250]
z = [300, 400, 100, 102, 104]

plt.scatter(x, y, s=200, color="g", alpha=0.3, label="First set")
plt.scatter(x, z, s=400, color="r", alpha=0.3, label="Second set")

plt.title('Random values')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.legend()

plt.show()