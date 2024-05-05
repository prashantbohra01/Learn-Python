#Some Problems 

# 1. W.A.P to get Fibonacci series upto 10 numbers. 

a = 0
b = 1

print(a)
print(b)

for i in range(2,11):
    c = a+b
    a = b
    b = c

    print(c) 


# 2. W.A.P to check if a number is prime or not. 

num = int(input("Enter a number here: "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, num):
        if num%i == 0:
            print("Number is not a prime number")
            break;
    else:
        print("It is a prime number.")

# 3. W.A.P to find a palindrome of integers. 

nums = int(input("Enter a number here: "))
temp = nums
rev = 0

while nums > 0:
    dig = nums%10
    rev = rev*10 + dig
    nums = nums // 10

if rev == temp:
    print("It is palindrome")
else:
    print("It is not a palindrome")


