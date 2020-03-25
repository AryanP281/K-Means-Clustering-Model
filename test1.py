#**************************Imports*********************
import numpy as np 
from K_Means_Model import K_Means_Model
import random
import matplotlib.pyplot as plt

#**************************Script Commands*********************

#Generating the inputs
inputs = np.zeros((40,2))
center = (0,0)
radius = 4
x_vals = np.arange(0, 4.1, 0.1)
for a in range(20) :
    x = x_vals[random.randint(0, x_vals.shape[0] - 1)]
    y_vals = np.arange(0, ((radius**2)-(x**2))**0.5, 0.1)
    if(y_vals.shape[0] == 0) :
        a -= 1
        continue
    inputs[a,0] = x
    inputs[a,1] = y_vals[random.randint(0, y_vals.shape[0] - 1)]
center = (8,0)
radius = 3
x_vals = np.arange(8, 4.9, -0.1)
for a in range(20, 40) :
    x = x_vals[random.randint(0, x_vals.shape[0] - 1)]
    y_vals = np.arange(0, ((radius**2)-((x-center[0])**2))**0.5, 0.1)
    inputs[a,0] = x
    inputs[a,1] = y_vals[random.randint(0, y_vals.shape[0] - 1)] 

#Getting clusters
kmns = K_Means_Model()
clusters, centroids, j = kmns.get_clusters(inputs, 3, 20)
for i in range(20) :
    new_res = kmns.get_clusters(inputs,3,20)
    if(new_res[2] < j) :
        clusters = new_res[0]
        j = new_res[2]

#Displaying the clusters
plt.plot(clusters[0][:,0], clusters[0][:,1], "r.")
plt.plot(clusters[1][:, 0], clusters[1][:,1], "b.")
plt.plot(clusters[2][:,0], clusters[2][:,1], "g.")
plt.xticks(range(0,15))
plt.show()