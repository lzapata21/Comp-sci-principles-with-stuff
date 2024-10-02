import random

# we define a function with a parameter called greeting
def randomPicker(greeting):
    # creating a list that lives only in this function
    nameList = []
    # getting names from user
    x = input(greeting)
    # add the name to this list
    nameList.append(x)
    y = input(greeting)
    nameList.append(y)
    z = input(greeting)
    nameList.append(z)
    # choose name from appended list
    randName = random.choice(nameList)
    # return that name to the function when called...
    return randName
print(randomPicker("Give me the rizzliest name you can think of "))
