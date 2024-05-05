#Some Problems on Strings

a = "Why fit in, When you are Born to Stand Out!"

# 1. W.A.P to find Length of the following string. 

print(len(a))

# 2. W.A.P to check how many times alphabet o is occuring. 

print(a.count("o"))

# 3. W.A.P to convert the whole string into lower and uppercases. 

b = a.lower()
c = a.upper()
print(b," ", c)

# 4. W.A.P to convert following string into a title. 

print(a.title())  # it will capitilise first letter of all the words in a string

# 5. W.A.P to find the index number of "fit in". 

print(a.find("fit in"))



# Pattern problem

for i in range(1,6):  # rows                #1
    for j in range(1,i+1): #columns         #12
        print(j, end=" ")                   #123
    print();                                #1234
                                            #12345

print("********************************************************")

# 2. Display below pattern. 

#1
#22
#333
#4444
#55555

for i in range(1,6):
    for j in range(1,i+1):
     print(i, end=" ")
    print()
print("**********************************************")

# 3. Display the pattern given below. 

#11111
#2222
#333
#44
#5

for i in range(1,6):
    for j in range(i,6):
     print(i, end=" ")
    print()

