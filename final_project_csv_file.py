import csv
import matplotlib.pyplot as plt

#creating variable
filename = 'WEEK5_PYTHON_FINAL_PROJECT/data.csv' #file name where data is kept. Used outworldindata.com to get data

population_per_continent = {}

{
    "Africa": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "Asia": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "Europe": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "North America": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]}
}

with open(filename, 'r') as csvfile: # we're only going to read the file as we're creating a graph from it
    reader = csv.DictReader(csvfile) # making a new variable for pythons DictReader object
    for line in reader:
        continent = line['continent'] #creating varibles so quicker to pass through print. For each row in the CSV, extract values for:
        year = line['year']
        population = line['population']
        
        if continent not in population_per_continent: #'contitnent' from above, looping through csv file. We want to store this object in our dictionary above, so have all the Africa populations calcualted together for eg. In order to do this we have to make sure the 'Africa' key already exists inside the dictionary
            population_per_continent[continent] = {'population': [], 'years': []} #recreating the structure. If 'Africa' in this case doesnt exists yet in the 'population_per_continent' variable, it is to make a new key called 'Africa' and include the population and years based on the structure i provided

        population_per_continent[continent]['population'].append(population)
        population_per_continent[continent]['years'].append(year)
        
print(population_per_continent)
        

        
# Data visuaisation
plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker="o") #adding
plt.plot([2000, 2010, 2020, 2030], [200, 300, 500, 800], label="Asia", marker="o")
plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid()
plt.legend()
plt.show()
