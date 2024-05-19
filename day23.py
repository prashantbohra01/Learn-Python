import json

student_data = {"name": "David", "age": 13, "marks": 87}  #JSON DATA


data= json.dumps(student_data)   # used to convert json dictionary into str 
print(type(student_data))
print(type(data))
print(data)

# Access the value of age from the given JSON data

data1= json.loads(data)
print(data1["age"])

# Pretty print following JSON data

data2= json.dumps(student_data, indent=4, separators=(",", "="))
print(data2)


