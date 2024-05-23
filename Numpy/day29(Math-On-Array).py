# Mathematical Operations and functions on arrays

import numpy as np 

arr1 = np.array([30, 40, 60, 20,60])
arr2 = np.array([30, 20, 10, 20, 30])
print(arr1+arr2) # Addition
print(np.add(arr1,arr2))

print(arr1-arr2) # Subtraction

print(arr1*arr2) # Multiplication

print(arr1/arr2) # Division 

arr3 = np.array([2])

print(np.power(arr1,arr3))  # arr3 becomes the power of arr1
print(np.sqrt(arr1)) # square root of arr1
