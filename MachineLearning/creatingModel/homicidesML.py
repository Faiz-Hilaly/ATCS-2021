"""
Create a Multiple Lieaner Regression
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''Load Data'''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/creatingModel/homicides.csv")

'''Create MLR Model'''
x = data[["Inhabitants", "Percent_with_income_below_5000", "Percent_unemployed"]].values
y = data["Murders_per_year_per_million"].values

#Split into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)

#Print model info
print("Inhabitants coef: ", model.coef_[0])
print("Low income coef: ", model.coef_[1])
print("percent unemployed coef: ", model.coef_[2])
print("Intercept: ", model.intercept_)

'''Test Model'''
#Get the predicted y values for x_test - return an array
predict = model.predict(x_test)

dev_sq_mdl = 0
dev_sq_avg = 0
avg = sum(y_test)/len(y_test)
#Compare the actual and predicted values
print("Testing Linear Model with Test Data: ")
for i in range(len(x_test)):
 	#Actual y value
	actual = y_test[i]
 	#Predicted y value
	y_pred = predict[i]
	dev_sq_mdl += (y_pred - actual)**2
	dev_sq_avg += (avg - actual)**2


print("deviation squared of model", dev_sq_mdl)
print("deviation squared of avg", dev_sq_avg)

#Test value
x_inhabitants = x_test[0][0]
x_low_income = x_test[0][1]
x_unemployed = x_test[0][2]
print("Inhabitants:", x_inhabitants, 
	"Low income:", x_low_income, 
	"Unemployed:", x_unemployed, 
	"Predicted murder rate:", predict[0], 
	"Actual murder rate:", y_test[0])

