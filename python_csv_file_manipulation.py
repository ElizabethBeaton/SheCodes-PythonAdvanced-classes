import csv

#creating the raw data
cities = [
    {"country": "France", "city": "Paris", "weather": 24},
    {"country": "Portugal", "city": "Lisbon", "weather": 30},
    {"country": "Australia", "city": "Canberra", "weather": 20}
]
#a list inside a dictionary ^


#storing the csv file field names
field_names = ['country', 'city', 'weather']

#storing the file name we want to create
file_name = 'cities.csv'

#create the file
with open(file_name, 'w') as csvfile:
    #create the writer
    writer = csv.DictWriter(csvfile, fieldnames=field_names) #creating a file write; file name will be 'cities.csv'. 'w' allows writing access. 'fieldnames' give its access/passes in all the field names as seen above that are inside the list
    writer.writeheader() #this allows the file to include the header (country,city,weather)
    writer.writerows(cities)#if this wasnt included, it wouldnt crash when ran, but the fil would be empty

#open the file
with open(file_name, 'r') as csvfile:
    #create the reader
    reader = csv.DictReader(csvfile)
    #read each line one by one
    for line in reader:
        print(line['country'])
        print(line['city'])
        print(line['weather'])
        #would print :
        """France
Paris
24
Portugal
Lisbon
30
Australia
Canberra
20"""