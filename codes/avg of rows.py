import numpy as np

n, p = [int(x) for x in input().split()]
arr = []

for i in range(n):
    arr.append(input().split())

print(np.array(arr).astype(np.float16).mean(axis = 1).round(2))
