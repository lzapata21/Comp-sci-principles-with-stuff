# create a list of names from table team
# randomly select from that list

# https://www.w3schools.com/python/python_lists.asp

# https://www.w3schools.com/python/module_random.asp

# you need to comment above each line of code to explain what it does

'''
this is a multi-line comment
See I can comment on multiple lines
'''

# to select a random name from the list of names in the table team
# you need to import the random library

# we import random library to get access to the functions and methods in the library
import random
from random import randint
from random import choice

# create a list of names from table team
myTables = ["0", "1", "2", "3"]
myTeamnames = ["Beavis", "Pac-man", "Butthead", "Homer", "Marge", "Bart", "Lisa", "Maggie"]
print(myTeamnames[random.randint(0, len(myTeamnames)-1)])
