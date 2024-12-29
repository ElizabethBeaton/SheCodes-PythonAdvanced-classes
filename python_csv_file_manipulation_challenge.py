import csv

weather = [
    {"city": "Paris", "country": "France", "temperature": 25},
    {"city": "New York", "country": "USA", "temperature": 23},
    {"city": "Berlin", "country": "Germany", "temperature": 22},
    {"city": "Bangkok", "country": "Thailand", "temperature": 35}
]

field_names = ["city", "country", "temperature"]

file_name = 'weather.csv'

with open(file_name, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(weather)
    
with open(file_name, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        print(f"It is currently {line['temperature']} degrees in {line['city']}, {line['country']}")
    
    






