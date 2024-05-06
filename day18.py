#___Tuples______

tup = (1,2,3,4)
tup1 = 1,2,3,4
print(type(tup), tup)
print(type(tup1), tup1)

'''
    Tuples are ordered collections of data items. They store multiple
    items in a single variable. Tuple items are separated by commas and 
    may or may not enclosed within round brackets(). Tuples are unchangable, 
    we can not alter after creation.
'''

if 4 in tup:
    print("yes")


#____Methods_of_tuples

'''
    Tuples are immutable, hence if you want to add, remove or change tuple items,
    then first you must convert tuple to a list. Then perform operation on that list 
    and convert it back to tuple.  
'''
countries = ("US", "Italy", "France", "India", "Japan")

temp=list(countries) # to convert tuple into list

temp.append("Australia") #add item
temp.pop(2) #remove item
temp[3]= "Russia" #change item

countries = tuple(temp) # to convert list into tuple

print(countries)  

# Count() method 
tuple=(0,1,2,3,5,1,3,1,0)
res=tuple.count(0)
print (res)

# index() method
res= tuple.index(5)
print (res)

# length() method
res= len(tuple)
print (res)

# Some Problems

Student_data = {"name":"David", "age":13, "marks": 87}
print(type(Student_data))

# 1. Convert the following dictionary into JSON format.

import json

data = json.dumps(Student_data)
print(data)
print(type(data))

# 2. Access the value of age from the given data. 

data = json.loads(Student_data)
print(data["age"])