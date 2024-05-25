# Aggregating Functions 

import numpy as np
import statistics as stats

a = np.array([20,40,60,80])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.mean(a))
print(np.cumsum(a)) # cumulative sum [ 20 60 120 200]
print(np.cumprod(a)) # cumulative product


# Statistical functions

baked_food = [200,300,150,130,200,280, 180,188]
b = np.array(baked_food)

print(np.mean(baked_food)) # sum of all the values divided by no. of values
print(np.median(baked_food)) 

# statistical 
print(stats.mode(baked_food)) 
print(np.std(baked_food))  # standard deviation, under root value

tobacco_consumption = np.array([30,50,10,30,50,40])
deaths = np.array([100,120,70,100,120,112])


print(np.corrcoef([tobacco_consumption,deaths]))