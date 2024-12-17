"""
    create a new TODO.txt file with some tsks you need to do
    display each item in a nice readable way using python
"""

with open('python_reading_files_challenge/todo.txt', 'r') as file:
    todo = file.readlines()

print("My todo list:")
for list in todo:
    print(f" - {list.strip()}")
    