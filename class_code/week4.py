import random

# we define a function with a parameter called greeting
def randomPicker(greeting):
    # creating a list that lives only in this function
    global nameList
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
#print(randomPicker("Give me the rizzliest name you can think of "))

randomPicker("type something here...")

print(nameList)

#namelist is in the function which cannot be accessed outside the funtion

#global allows function to be accessed outside function

x = 1

x != 1

# This loop uses break to run one time then be done 


while x < 5:
    print("infinite loops are dangerous...")
    
    x+=1
    break