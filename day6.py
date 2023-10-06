#______________________USER_INPUT______________________


a=input("Enter your name:") # We can directly take input from the user by using input() function.
print("My name is " + a)



x=input("Enter first number: ")
y=input("Enter second number: ")

print(x + y) 
''' Now this will concatenate the numbers because in python
 if we are taking direct input it will be in string format.'''

# So to avoid these problems we can use Typecasting.

print(int(x)+int(y))

# Also we can use the typecasting before the input () function.

z=int(input("Enter first number:"))
v=int(input("Enter second number:"))

print(z+v)