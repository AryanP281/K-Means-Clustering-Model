#**************************Import*********************
import numpy as np 
import matplotlib.pyplot as plt
from K_Means_Model import K_Means_Model

#**************************Script Commands*********************

#Reading the data
data_file = open("data.txt", "r")
data = []
while True :
    line = data_file.readline()

    if(line == "") :
        break

    data.extend(list(map(int,line.split(',')[:-1])))    

X = np.array(data)
X.shape = ((int)(len(data) / 5), 5)

#Visualizing the data
plt.plot(X[:, 3], X[:, 4], "k.")
plt.show()

#Finding Clusters
kmns = K_Means_Model()
k = 5
x1 = X[:,3]
x1.shape = (len(x1), 1)
x2 = X[:, 4]
x2.shape = (len(x2), 1)
clusters,centroids,j = kmns.get_clusters(np.concatenate((x1, x2), axis=1), k, 100)
for i in range(20) :
    new_res = kmns.get_clusters(np.concatenate((x1, x2), axis=1), k, 100)
    if(new_res[2] < j) :
        clusters = new_res[0]
        j = new_res[2]

#Displaying the clusters
colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
for a in range(k) :
    plt.plot(clusters[a][:, 0], clusters[a][:, 1], f"{colors[a % (len(colors))]}.")

plt.show()