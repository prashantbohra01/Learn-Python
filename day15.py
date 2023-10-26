#__________Function__________

'''
Syntax for functions = def FunctionNAme(0):

Function is a block of code that performs a specific task whenever it is called.
In Bigger programs, where we have large amounts of code it is advisable to create or use 
existing functions that make the program flow organized and neat.
'''

def CalculateGmean(a, b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if (a>b):
        print("First No. is greater")
    else:
        print("Second No. is greater")


a=8
b=6

isGreater(a,b)
CalculateGmean(a,b)

c=81
d=98

isGreater(c,d)
CalculateGmean(c,d)