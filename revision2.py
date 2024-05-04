# 1. W.A.P to check if no. is positive. 

a = int(input("Enter a no.: "))

if a>0:
    print("no. is positive")
else:
    print("no. is negative")

# 2. W.A.P to check whether a number is odd or even

a= int(input("Enter a no.: "))

if a%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

# 3. W.A.P to check whether the passed letter is a vowel or not.

word = input("Enter a character: ")

if (word in "aeiou") or (word in "AEIOU"):
    print("It is a vowel")
else:
    print("It is not a vowel")

# 4. W.A.P to check if a number is a single digit number, 2 digit and so on... , up to 5 digits.

num = int(input("Enter a number here upto 5 digits: "))

if num>=0 and num <=9:
    print("it is a single digit number")
elif num>=10 and num <=99:
    print("it is a two digit number")
elif num>=100 and num <=999:
    print("it is a three digit number")
elif num>=1000 and num <=9999:
    print("it is a four digit number")

else: print("It is 5 digit or greater than 5 digit number")