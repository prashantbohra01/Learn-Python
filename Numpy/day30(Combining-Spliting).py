#Combining and Splitting of array 
import numpy as np

a1 = [30,40,50]
b1 = [5,5,3]
# print(a+b) # concatenate using "+"" in list

arr1 = np.array([30,40,50])
arr2 = np.array([5,5,3])
# print(np.concatenate([arr1,arr2])) # to concatenate in numpy without comma separation. 

print(np.hstack([arr1,arr2])) # horizontal concatenation
print(np.vstack([arr1,arr2])) # vertical concatenation


a = np.array([20,40,30,40,10,20])
b= np.array_split(a,3)
print(b[2])


# Adding and Removing elements in array

a2 = np.array([20,40,60,80])  
print(np.append(a2,[90,100]))   #  Add values at the end of the array

print(np.insert(a2 ,1, 50 ))  # to insert a value in the array anywhere using the syntax np.insert(array, index, value)

print(np.delete(a2,1))

