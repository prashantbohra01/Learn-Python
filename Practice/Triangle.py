# In this we are making a right angle triangle using *

a = "*"

for i in range(5):
    for j in range(i+1):
        print(a, end="")
    print()

print()  # using only to seperate the outputs 

# Here we are making same right angle triangle using numbers

for i in range(5):
    for j in range(1, i+2):
        print(j, end="")
    print()

print()  # using only to seperate the outputs 

# Here we are making same right angle triangle using same number in a line 

for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

print()  # using only to seperate the outputs 

# Here we are making a reverse right angle triangle

n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

print()  # using only to seperate the outputs 

# Here we are making a inverted half pyramid 

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    
    for k in range(i+1):
            print("*", end="")
    print()