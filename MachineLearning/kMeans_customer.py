import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

'''Load Data'''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/kMeans_customer.py")
x = data[["Annual Income", "Spending Score"]]

#Standardize Data
scaler = StandardScaler().fit(x)
x = scaler.transorm(x)

''' Determine the value for K '''
#Calculate the interia for K=1 to 10
inertias = []
for k in range(1, 11):
	#Build and fit the model
	kmeanModel = KMeans(n_clusers=k).fit(x)
	#Store the inertias
	inertias.append(kmeanModel.interia_)

#Plot the interias to find the elbow
plt.plot(range(1,11), inertias, 'bx-')
plt.xlabel("Values of K")
plt.ylabels("Inertia")
plt.show()

'''Create the Model'''
#From the elbow method
k = 5
km = KMeans(n_clusers=k).fit(x)

#Get the centroids and label values
centroids = km.cluster_centers_
labels=km.labels_

''' Visualize the CLuster'''
plt.figure(figsize=(5,4))

#Plot the data points for each of the k clusters
for i in range(k):
	# Get all the points x[n] where labels[n] == the label i
	cluster = x[labels == i]
	#Get the income and spending values for each point in the cluster
	cluster_income = cluster[:, 0]
	cluster_spending = cluster[:, 1]
	plt.scatter(cluster_income, cluster_spending)

#plot the centroids
centroids_income = centroids[:, 0]
centroids_spending = centroids[:, 1]
plt.scatter(centroids_income, centroids_spending, marker = 'X', s = 100, c = 'r')

#plt.scatter(x[:, 0], x[:, 1])
#plt.xlabel("Annual Income")
#plt.ylabel("Spending Score")
#plt.show()