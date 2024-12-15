"""
Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
Test both classes
Move each class into their files
"""


from french_user import FrenchUser
from spanish_user import SpanishUser

gabs = FrenchUser("Gabs")
gabs.greet()

SpanishUser = SpanishUser("Liz")
SpanishUser.greet()