"""
@author: Faiz Hilaly
@version: 02/23/2022
@source: CodeHS
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

''' Load Data '''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/blood_pressure.csv")

''' TODO: Create Linear Regression '''
# Get the values from x and y
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)


# Create the model
model = LinearRegression().fit(x, y)

# Find the slope and intercept
# Each should be a float and rounded to two decimal places.
slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)

# Print out the linear equation
print("y= ", slope, "x + ", intercept)

# Predict the the blood pressure of someone who is 43 years old.
print("BP of someone who is 43 y/o: ", slope * 43 + intercept)

# Print out the prediction

''' Visualize Data '''
# set the size of the graph
plt.figure(figsize=(5, 4))

# label axes and create a scatterplot
plt.xlabel("Age")
plt.ylabel("Systolic Blood Pressure")
plt.title("Systolic Blood Pressure by Age")
plt.scatter(x, y)
plt.show()

print("Pearson's Correlation: r = :", x.corr(y))
