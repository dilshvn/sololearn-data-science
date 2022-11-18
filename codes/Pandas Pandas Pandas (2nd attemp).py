import numpy as np
from sklearn.cluster import KMeans

n = int(input())
ls0 = []
ls1 = []
matrix = []

for i in range(n):
    matrix.append(input().split())

X = np.array([[0, 0], [2, 2]], dtype='float64')
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
j=0

for i in kmeans.predict(matrix):
    if i == 0:
        ls0.append(matrix[j])
    if i == 1:
        ls1.append(matrix[j])
    j+=1

result1 = np.round(np.array(ls0).astype(float), 2)
result2 = np.round(np.array(ls1).astype(float), 2)  

if len(ls0) == 0:
    print('None')
else: 
    kmeans1 = KMeans(n_clusters=1, random_state=0).fit(result1)
    print(np.round(np.array(kmeans1.cluster_centers_[0]).astype(float), 2))

if len(ls1) == 0:
    print('None')
else:
    kmeans2 = KMeans(n_clusters=1, random_state=0).fit(result2)
    print(np.round(np.array(kmeans2.cluster_centers_[0]).astype(float), 2))