#_________IF_ELSE_CONDITIONAL_STATEMENT______________

a=int(input("Enter your age: "))
print("your age is: ", a)

if(a>18):
    print("you can drive")
else:
    print("you can not drive")


  # else if  is used for multiple conditions for example:

num= int(input("Enter a value for num: "))
     
if (num < 0):
    print("Number is negative")
elif (num==0):
    print("Number is Zero")    #we can use multiple elif for multiple conditions.
elif (num==999):
    print("Number is Special Number")
else:
    print("Number is Positive")
       

# Nested if else condition.

no=int(input("Enter a number: "))

if(no<0):
    print("Number is Negative")

elif(no>0):
    if(no<=10):
        print("Number is between 0 and 10")
    elif(no>10 and no<=20):
        print("Number is between 10 and 20")
    else:
        print("Number is greater than 20")

else:
    print("Number is zero")