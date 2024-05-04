''' #for multi comment use three """text here"""
print("hello")
print("""Hello 
      guys
      Coders...""")

a= "Hello"
print(a)

name = input("Enter your name here: ")
print(name)

age = int(input("Enter your age: "))
print(age)

exp1 = eval(input("Enter any equation here: "))
print(exp1)
'''
#Type Casting
# Conversion of one datatype to another 
# Two types of typeCasting : 1.Implicit type conversion, 2. Explicit type conversion

name = "Prashant"
age = 23
print(type(name))
print(type(age))

a="123"
b=1.23
print(type(a))
print(type(b))

a= float(a)            # Explicit conversion of a sting type into integer
print("after conversion", type(a))

c= a+b
print(type(c))


#some problems

# 1. W.A.P to Swap two variables.
a = 21
b = 10

temp = a
a = b
b = temp
print("a=",a,"b=",b)

# 2. W.A.P to convert float into integer

a = 1.25
print(int(a))

#3. W.A.P to take details from a student for ID-card and then print it in different lines.

print("Student Identity Card")
name = input("Enter the name of student: ")
grade = input("Enter the grade of student: ")
age = input("Enter the age of student: ")
ph = input("Enter the ph no. of student: ")



