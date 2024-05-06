# List Comprehension

l1 = [30, 40, 50, 60]
l2 = []

for i in l1:
    if i > 45:
        l2.append(i)

print(l1, "\n", l2)

l3 = [i for i in l1 if i > 35]    #list comprehension used to copy data from 1 list to another. 
print(l3)


# Some Problems

A = ["Ross", "Rachel", "Monica", "Joe"]

# 1. W.A.P to swap first amd forth element. 

A[0], A[3] = A[3], A[0]
print(A)

# 2. W.A.P to add a new value at second position. 

A.insert(1,"Michal")
print(A)

# 3. W.A.P to delete a value from 3rd position.

A.pop(2)
print(A)

# 4. W.A.P to multiply all the numbers in the list. 

B = [13,7,12,10]
mul = 1
for i in (B):
    mul*=i
print(mul)

# 5. W.A.P to get the largest number from the list. 

B.sort()
print(B)

print("The largest value in given list is", B[-1])



