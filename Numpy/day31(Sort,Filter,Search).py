# Sort, Filter and search

import numpy as np

arr = np.array([7,5,2,6,3,8,4,1])
print(np.sort(arr))

s = np.where(arr==4) # search the element index 
s1 = np.where(arr % 2 == 0) # seach the element index which is divisible by 2 and give 0 as remainder
print(s)
print(s1)

ss = np.searchsorted(arr,5)
print(ss)

# Filter

arr1 = np.array([20,30,40,50,60,70,80])

filteredArray = [True, False, True, False, True, False, True]
filteredArray1 = arr1>35
filteredArray2 = arr1 % 3 == 0

newarr = arr1[filteredArray]
newarr1 = arr1[filteredArray1]
newarr2 = arr1[filteredArray2]

print(newarr)
print(newarr1)
print(newarr2)