try:
    file = open('citiess.txt', 'r')
    
    content = files.read()
except FileNotFoundError:
    print("cannot find the file")

print("hello world")
    
try:
    12 / 0
except ZeroDivisionError:
    print('cannot divide number by 0')
    
    
try:
    a + b
except Exception:
    print('cannoy divide by 0')
    
    
    
    
    
    
    """
    good to use if youre using a large file/api and you're notiving some issues, this will test/try it, and using the except so the code can continue working
    ideally, dont use 'exception' as an exception bevause this catches all the problems. better to use soething more specific like FileNotFoundError or ZeroDivisionError for eg
    """
    
    
"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.    
    """

"""
    Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
    """
"""
Else
You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")    
    """
    
"""
Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.

Example
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
    """

"""
This can be useful to close objects and clean up resources:

Example
Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")    
    """
    
    