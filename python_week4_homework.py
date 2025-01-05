#function to calculate the overall population total. 
def calculate_total_population(population_list): #good habit is to start function with a verb
    total = 0 #initialise the total amount to 0
    for population in population_list: #iterate through each dictionary in the populations list
            total = total + int(population["population"]) #adding all the population amount totals once onverted to an integer and assigned to the total variable
        
    return round(total) #this will return the amount. 
        

def display_total_population(total):
    #display total population and diide by 1 million to display output we want 
    total_population_in_millions = total // 1000000
    print(f"The total population is {total_population_in_millions} million people") #displaying 203 million instead of 203000000

#list of dictionaries. initial data set
populations = [
    { 'country': "France", "population": "60000000"},
    { 'country': "Spain", "population": "50000000"},
    { 'country': "USA", "population": "30000000"},
    { 'country': "Australia", "population": "25000000"},
    { 'country': "Canada", "population": "38000000"},
]

#display the total population
total_population = calculate_total_population(populations)  #calling the first function
display_total_population(total_population)  #calling the second function






#print(f"The total population is {total_population}")
"""
right now need to get it adding all the total
then can add a function with makes the total appear like 203 million, instead of 20300000
will need to adjust the print statement too
"""






"""
loop through dictionary
remember to convert number string into int
add to total pop variable
use slice to only write first 3 digits ?
change print statement
"""







"""
    when we would and would not use return in function:
    
    you would use a return statement in a function to provide a rsult or put output back to the caller
    this is particularly useful when the function performs a calculation, retrieves some data, or processes input that the rest of th eprogram needs to use.
    in our instance above, we wrote 'return round(total)' because we would need this in our print statement later. 
    as this return is in the 'calculate_total_population' function, thats why later we have:
    
    total_population = calculate_total_population(populations)

display_total_population(total_population) 

where the total population is the new variable created that has the 'tota' from the 'calculate_total_population' function, passed through the 'populations' list of dictionaries


 another example of a reason 'result' would needed to be written:
 
 def add(a, b):
    return a + b

def double(number):
    return number * 2

result = double(add(3, 4))  # The result of `add` is passed to `double`.
print(result)               # Output: 14



An example of an instance where 'return' wouldnt need to be written:

def greet(name):
    print(f"Hello, {name}!")  # Performs a side effect (printing)
greet("Alice")  # Output: Hello, Alice!

    """