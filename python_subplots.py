import matplotlib.pyplot as plt


fig, (ax1, ax2) = plt.subplots(2,1)
#(plt.subplot(2,1) means therell be two rows, one column. 
# if it was (1,2), there woud be one row, two columns - side by side)

x = [1, 2, 3, 4, 5]
y = [12, 13, 10, 8, 6]
z = [50, 23, 25, 36, 10]

ax1.plot(x, y, color="r", label="Y values")
ax1.plot(x,z)
#can still have multiple plots in one graph even with subplots
ax2.plot(x, z, color="g", label="Z values")

ax1.set_title("Y growth")
ax1.legend()
ax2.set_title('Z growth')
ax2.legend()

plt.tight_layout()
#good to use this when creating subplots as it helps make the graphs more readable
#eg if we didnt use this, the title for graph 2 would overlap

plt.savefig("output.png")
#this saves the image into your file^
plt.show()

