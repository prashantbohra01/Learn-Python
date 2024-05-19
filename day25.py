# Sets 

# Sets are unordered collection of data. Every elements inside the set is unique and mutable.
# Sets are written inside the curly brackets. 
# The values inside a set is separated by comma(,)
# Mutable means once created, they can be changed. 

a = {"Ironman", "Hulk", "Thor", "Captain America"} # o/p will be different everytime because their is no indexing in sets.
print(a)

for x in a:
    print(x)

# Functions in sets

# 1. add()
 
a.add("Spiderman")
print(a)

# 2. pop()

a.pop() # it will randomly removes a value
print(a)

# 3. remove()

a.remove("Thor") # it will remove particular given value
print(a)

# 4. discard()

a.discard("Hulk") # same as remove function
print(a)

# 5. copy

b = a.copy()
print(b)


# example 2:

x = {"Bigchill", "X", "Cannonbolt", "Waybig"}
y = {"Stinkfly", "Ghostfreak", "wildmut"}
z = {"X", "Raph"}

# 6. isdisjoint() # This functions check is their is value present in another set or not

print(x.isdisjoint(y))

# 7. issubset()

print(x.issubset(y))


# Problems

# WAP to find max and min in a set

num = {12,56,21,74,4,1}
maximum = max(num)
minumum = min(num)

print(maximum)
print(minumum)

# WAP to find common elements in three lists using sets. 

s = [1,2,4,5,7,3]
d = [4,5,6,7]
f = [1,9,2,5,6,7]

print(set(s) & set(d) & set(f))