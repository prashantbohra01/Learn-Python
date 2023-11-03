#_____Recursion__________

# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1

# factorial(n) = n * factorial(n-1)  

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))

print(factorial(0))

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

#fibonacci sequence

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)

#f(n) = f(n-1) + f(n-2) 

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))



     

