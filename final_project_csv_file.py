import csv
import matplotlib.pyplot as plt

#creating variable
filename = 'WEEK5_PYTHON_FINAL_PROJECT/data.csv' #file name where data is kept. Used outworldindata.com to get data

with open(filename, 'r') as csvfile: # we're only going to read the file as we're creating a graph from it
    reader = csv.DictReader(csvfile) # making a new variable for pythons DictReader object
    for line in reader:
        
        continent = line['continent'] #creating varibles so quicker to pass through print
        year = line['year']
        population = line['population']
        
        print(continent)
        print(year)
        print(population)
        
# Data visuaisation
plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker="o") #adding
plt.plot([2000, 2010, 2020, 2030], [200, 300, 500, 800], label="Asia", marker="o")
plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid()
plt.legend()
plt.show()