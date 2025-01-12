import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
    """
    
    Generate population dictionary from csv data
    Return a dictionary following this structure
    {
    "Africa": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "Asia": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "Europe": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]},
    "North America": {'population': [100, 200, 300], 'years': [2000, 2010, 2020]}
}
    """
    population_per_continent = {}
    


    with open(filename, 'r') as csvfile: # we're only going to read the file as we're creating a graph from it
        reader = csv.DictReader(csvfile) # making a new variable for pythons DictReader object
        for line in reader:
            continent = line['continent'] #creating varibles so quicker to pass through print. For each row in the CSV, extract values for:
            year = int(line['year']) #converting these strings to integers. plot has issues rendering
            population = int(line['population']) #^
        
            if continent not in population_per_continent: #'continent' from above, looping through csv file. We want to store this object in our dictionary above, so have all the Africa populations calcualted together for eg. In order to do this we have to make sure the 'Africa' key already exists inside the dictionary
                population_per_continent[continent] = {'population': [], 'years': []} #recreating the structure. If 'Africa' in this case doesnt exists yet in the 'population_per_continent' variable, it is to make a new key called 'Africa' and include the population and years based on the structure i provided

            population_per_continent[continent]['population'].append(population)
            population_per_continent[continent]['years'].append(year)

    return population_per_continent


def generate_population_plots_from_dictionary(population_dictionary):
    
    """
    Generate the population plot from a dictionary
    One plot per continent
    
    """
    
    for continent in population_per_continent:  #going through each continent we stored in our dictionary, 
        years = population_per_continent[continent]['years'] #we extracted the years and population of each continent
        population = population_per_continent[continent]['population']
        plt.plot(years, population, label=continent, marker="o", alpha=0.7) #then put this data inside a plit based on years and population. years as x axis and users in y axis
        
    plt.title("Internet Population per Continent")
    plt.xlabel("Year")
    plt.ylabel("Internet Users (in billion users)")
    plt.grid(True)
    plt.legend()
    plt.show()
    


#creating variable
filename = 'WEEK5_PYTHON_FINAL_PROJECT/data.csv' #file name where data is kept. Used outworldindata.com to get data


#display internet population in the plot
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)




