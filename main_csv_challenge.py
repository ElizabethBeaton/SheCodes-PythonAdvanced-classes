"""
    Read temperatures.csv and display the temperatures following this format:
“It is cloudy and 12ºC in Toronto”
"""

import csv

with open('python_csv_file_challenge.csv', 'r') as temps_file:
    csv_reader = csv.reader(temps_file)
    
    for temperatures in csv_reader:
        print(f"It is {temperatures[2]} and {temperatures[1]} in {temperatures[2]}")