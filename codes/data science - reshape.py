import numpy as np

r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)

arr = arr.reshape(r,-1)
print(arr)