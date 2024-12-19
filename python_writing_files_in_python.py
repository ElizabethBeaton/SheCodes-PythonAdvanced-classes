#write new lines into a file
file = open('cities.txt', 'w')

file.write('Lisbon\n')
file.write('Paris\n')
file.write('New York\n')

file.close()

#append new lines into a file

file = open('cities.txt', 'a')
file.write('Tokyo\n')
file.write('Paris\n')

with open('cities.txt', 'w') as file:
    file.write('lisbon\n')