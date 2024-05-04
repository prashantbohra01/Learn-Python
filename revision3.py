'''
# for Loop

for i in range(1,6,2):   # the third input is used to give tha gap between given range.
    print(i)

n = 9
for i in range(1,11):
    print(n, "x", i, "=", n*i)

# While Loop

n = 1
while n<=5:
    print(n)
    n += 1


a = 1
b = 7
while a<=10:
    print(b, "x", a, "=", b*a)
    a+=1

# Nested Loop

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end ="")
    print()
    
# BREAK:

for i in range(12):
 if( i == 10):
   break
 print("5 x", i+1, "=", 5*(i+1))

print("Exited from loop")


# Continue:

for i in range(12):
  if( i == 0):
    print("skipping this iteration")
    continue
  print("5 x", i, "=", 5*i)

'''
# Some Problems

# 1. W.A.P to find sum of all the even numbers upto 50.

sum = 0
for i in range(1,51):
    if i%2==0:
        sum += i

print("The sum of all even numbers upto 50 is:",sum)

# 2. W.A.P to write first 20 numbers and their squared numbers.

for i in range(1, 21):
    print (i, i*i)

# 3. W.A.P to find sum od first 10 odd numbers using while loop. 

sumOdd = 0
n = 0
odd_numbers = [] # Empty array/list to store the numbers
while n<=20:
    if n%2 != 0:
        sumOdd += n
        odd_numbers.append(n) # Append the odd number to the list
    n += 1

print("The odd numbers added are:", odd_numbers)
print("Sum of first 10 odd number is:", sumOdd)

# 4. W.A.P to create a billing system at supermarket. 

while True:
        Name = input("Enter customer's name: ")
        total = 0
        
        while True:
            print("Enter the amount and quantity")
            amount=float(input("Enter amount: "))
            quantity=float(input("Enter quantity: "))
            total += amount*quantity
            repeat = input("Do you want to add more items? (Yes/No): ")
            if repeat == "no" or repeat == "No":
                 break
        
        print("-"*40)
        print("Name: ", Name)
        print("Amount to be paid: ", total)
        print("-"*40)
        print("************Happy Shopping**********")

        repeat1 = input("Do you want to go to next customer? (Yes/No): ")
        if repeat1 == "no" or repeat1 == "No":
         break