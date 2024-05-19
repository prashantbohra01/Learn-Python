# Dictionary

# Dictionary allows user to write the data in te form of keys and values.
# Dictionaries are enclosed inside the curly brackets{}
# keys and values are separated by colon
# Every key value pair is separated by a coma(,)

Employee_data = {"name": "John", "age": 21, "gender": "male"}
print(Employee_data)

print(Employee_data["name"])

# Iterations in Dictionary

student = {"name": "Prashant", "class": "Btech", "roll_no": 21}

# Printing all the key names one by one

for x in student:
    print(x)

# Print all the values names one by one

for x in student:
    print(student[x])

# Value function

for x in student.values():
    print(x)


# Functions in Dictionary 

# get

x = student.get("name")
print(x)

# item

a = student.items()
print(a)

# keys

b = student.keys()
print(b)

# values

c = student.values()
print(c)

# copy

d = student.copy()
print(d)

# setdefault

e = student.setdefault("rank", 32)
print(e)


# Nested Dictionaries

Emp = {1: {"Name": "John", "Age": 20},
       2: {"Name": "Lisa", "Age": 21},
       3: {"Name": "Peter", "Age": 22}}

print(Emp[2]["Name"])