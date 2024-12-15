""""
Fork the reply, move the class user into its own file and import to make sure it works.
"""

from user import User

nancy = User("Nancy", 1998)
print(nancy.welcome())

luiza = User("Luiza", 2005)
print(luiza.welcome())
