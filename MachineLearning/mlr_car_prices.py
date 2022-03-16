"""
A Machine Learning algorithm to predict car prices

@author: Faiz Hilaly
@version: 02/23/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


''' Load Data '''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/car.csv")
x_1 = data["miles"]
x_2 = data["age"]
y = data["Price"]

''' Visualize Data '''
fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Total Miles")
graph[0].set_ylabel("Price")

graph[1].scatter(x_2, y)
graph[1].set_ylabel("Price")
graph[1].set_xlabel("Car Age")

print("Correlation between Total Miles and Car Price:", x_1.corr(y))
print("Correlation between Age and Car Price:", x_2.corr(y))

#plt.tight_layout()
plt.show()

''' TODO: Create Linear Regression '''
# Reload and/or reformat the data to get the values from x and y
x = data[["miles", "age"]].values
y = data["Price"].values

# Separate data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create multivariable linear regression model
model = LinearRegression().fit(x_train, y_train)

# Find and print the coefficients, intercept, and r squared values.
# Each rounded to two decimal places.
print(model.coef_)
print(model.intercept_)

y_train_pred = model.predict(x_train)
train_error = sum((y_train - y_train_pred)**2)
y_train_avg = sum(y_train)/len(y_train)
untrain_error = sum((y_train - y_train_avg)**2)
frac_not_working = train_error/untrain_error
n = len(y_train)
k = 2
adjusted_frac = frac_not_working*(n-1)/(n-k-1)
r_sq = 1-frac_not_working
adjusted_r_sq = 1-adjusted_frac

print("This is r squared:", r_sq)
print("This is adjusted r squared:", adjusted_r_sq)


# Test the model
#Compare the actual and predicted values
print("Testing Linear Model with Test Data: ")
y_pred = model.predict(x_test)
for i in range(len(x_test)):
	#Actual y value
	actual = y_test[i]
	#Test value
	miles = x_test[i][0]
	age = x_test[i][1]
	print("Miles: ", miles, " Age: ", age, " Predict y val:", y_pred[i], "Actual y value:", actual)

print("Price of 10 y/o car w 89000 miles:", model.intercept_ + model.coef_[0]*89000 + model.coef_[1]*10)
print("Price of 20 y/o car w 150000 miles:", model.intercept_ + model.coef_[0]*150000 + model.coef_[1]*20)


# Print out the actual vs the predicted values
plt.tight_layout()
plt.show()
