import numpy as np

n = int(input())
i = 0
data = []
dist1 = []
dist2 = []

while i < n:
    input_ = input().split()
    data.append(input_)
    i += 1

for p in data:
    dist = (float(p[0])**2 + float(p[1])**2)**(0.5)
    dist1.append(dist)
    dist = ((float(p[0]) - 2)**2 + (float(p[1]) - 2)**2)**0.5
    dist2.append(dist)

clust1 = []; clust2 = []

for i in range(n):
    if dist1[i] > dist2[i]:
        clust2.append(data[i])
    elif dist1[i] <= dist2[i]:
        clust1.append(data[i])

final_clust1 = []
temp1 = temp2 = 0

for i in clust1:
    temp1 += (float(i[0])/len(clust1))
    temp2 += (float(i[1])/len(clust1))
final_clust1.append(temp1)
final_clust1.append(temp2)

final_clust2 = []
temp1 = temp2 = 0

for i in clust2:
    temp1 += (float(i[0])/len(clust2))
    temp2 += (float(i[1])/len(clust2))
final_clust2.append(temp1)
final_clust2.append(temp2)

if final_clust1 == [] or final_clust2 == []:
    print(None)
else:
    final_clust1 = np.array(final_clust1)
    print(np.round(final_clust1, 2))
    final_clust2 = np.array(final_clust2)
    print(np.round(final_clust2, 2))

