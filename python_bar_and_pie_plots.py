import matplotlib.pyplot as plt

languages = ["French", "English", "Spanish", "Portuguese", "Greek", "Chinese"]
counts = [10, 40, 30, 20, 5, 15]


plt.pie(counts, labels=languages)

plt.ylabel('Speakers')
plt.title('Native speakers in the classroom')


plt.show()