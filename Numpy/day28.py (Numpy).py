# Numpy is the sort form of Numerical Python. 
# In 2005, Travis Oliphant created Numpy Package. 
# Numpy is a package that defines a multi dimensional array object and 
# associates fast math functions that operate  on
# It also has functions for working in domain of linear Algebra, fourier transformation and Matrices. 
# In simple words, it is fundamental package for scientific computing in python. 



# Arrays in numpy
# 1. An array is defined as a collection of items that are stored at *CONTIGUOUS* memory locations. 
# 2. It is a container which can hold a fixed number of items, and these items should be of same type. 
# 3. A combination of arrays saves a lot of time. The array can reduce the overall size of code. 

import numpy as np

# normal list array 
l1 = [20,30,40]
l2 = [50,60,70]
print(l1+l2)  # concatenating both list

# array using numpy
a = np.array([20,30])
b = np.array([40,50])
print(a)  # output without any separation coma 
print(b)  # output without any separation coma 
print(a+b)  # Addition of both Arrays. 


# Slicing of array

arr = np.array([10,20,30,40])
# print(arr[1])
# print(arr[1:3])
# print(arr[0:3])

arr1 = np.array([[10,20,30,40],[50,60,70,80]])
print(arr1[0:2,1:4])