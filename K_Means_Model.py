#**************************Imports*********************
import numpy as np
from copy import deepcopy

#**************************Class*********************
class K_Means_Model(object) :

    def __init__(self) :
        pass
    
    def get_clusters(self, X, k, epochs) :
        """Finds clusters in the given data
        X = a numpy matrix containing the data (m X n)
        epochs = the number of epochs to run the algorithm for
        k = number of clusters to be found
        return (clusters, centroids, j), clusters = list containing the data arranged in clusters, 
        centroids = numpy matrix containing the centroids, j = value of cost function"""

        #Initializing the centroids
        centroids = self.randomly_initialize_centroids(X, k)

        c = None #The clusters found
        j = 0 #The value of the cost function
        for epoch in range(epochs) :

            #Getting the nearest centroid for each point
            c,j = self.get_nearest_centroids(X, centroids)

            #Calculating the new positions for the centroids
            old_centroids = deepcopy(centroids)
            for centroid in range(k) :
                datapoints = X[np.where(c==centroid),:][0] #Getting the datapoints nearest to the centroid
                
                #Calculating the new centroids
                centroids[centroid] =  np.sum(datapoints, axis=0) / datapoints.shape[0]

            #Checking if the clusters have been found
            if(np.array_equal(centroids - old_centroids, np.zeros(centroids.shape))) :
                break 

        return (self.arrange_clusters(X, c, k), centroids, j)


    def randomly_initialize_centroids(self, X, k) :
        """Returns random points from the dataset as initializations for the centroids
        X = a numpy matrix containing the data (m X n)
        k = number of clusters to be found"""

        rands = np.random.randint(0, X.shape[0], size=k) #Randomly selecting points from dataset
        rands.shape = (1, k)

        return X[rands[0, :], :]

    def get_nearest_centroids(self, X, centroids) :
        """ Returns the nearest centroids for the points in the datasets
        X = a numpy matrix containing the data (m X n)
        centroids = a numpy matrix containing the centroids (k X n)
        returns (c,j), c = nearest centroids for the datapoints, j = value of cost function 
        """

        dist = np.zeros((X.shape[0], centroids.shape[0])) #A matrix containing the distance between each datapoint and centroid (m X k)

        #Calculating the distances from the centroids
        for i in range(X.shape[0]) :
            for k in range(centroids.shape[0]) :
                l = np.sum((X[i]  - centroids[k])**2)
                dist[i,k] = l

        #Getting the nearest centroids for the datapoints
        c = np.argmin(dist, axis=1)

        #Calculating the cost function value
        j = (1/X.shape[0]) * np.sum(np.min(dist, axis=1))

        return (c,j)

    def arrange_clusters(self, X, c, k) :
        """Arranges the found clusters"""

        clusters = []
        for a in range(k) :
            clusters.append(X[np.where(c==a),:][0])

        return clusters

