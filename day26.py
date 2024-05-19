# Functions

# Functions are set of code which once created they can be used throughout the program. 
# Functions help break our program into smaller parts and helps it look more organized and manageable. 

def hello():
    print("hello")

hello()

def add():
    x=12
    y=15
    print(x+y)

add()

# Parameters:
# Parameters are the variables written inside the parentheses with the name of function. 

# Arguments:
# Arguments are the values passed to the parameters while calling the function. 

def sum(x,y): # parameters 
    print(x+y)

sum(10,25) # arguments


# Return statement 
# return keyword in python is used to exit a function and return the value of the function. 

def helo():
    return("YO")

print(helo())

def addition(a,b):
    return(a+b)

print(addition(10,25))


# Lambda function
# It is used when an anonymous function is req for a short period of time
# it can take numerous arguments
# it can have only one expression

a= lambda b: b*5

print(a(10))    