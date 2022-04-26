"""
Create a Multiple Lieaner Regression
model to predict the Fawn population
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''Load Data'''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/antelope.csv")
x_1 = data["Annual Precipitation"]
x_2 = data["Winter Severity"]
y = data["Fawn"]

fig, graph = plt.subplots(2)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Annual Precipitation")
graph[0].set_ylabel("Fawn")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Winter Severity")
graph[1].set_ylabel("Fawn")

print("Corr between Annual Precipitation and Fawn: ", x_1.corr(y))
print("Corr between Winter Severity and Fawn: ", x_2.corr(y))

'''Create MLR Model'''
x = data[["Annual Precipitation", "Winter Severity"]].values
y = data["Fawn"].values

#Split into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)

#Print model info
print("Annual Precipitation coef: ", model.coef_[0])
print("Winter Severity coef: ", model.coef_[1])
print("Intercept: ", model.intercept_)

'''Test Model'''
#Get the predicted y values for x_test - return an array
predict = model.predict(x_test)

#Compare the actual and predicted values
print("Testing Linear Model with Test Data: ")
for i in range(len(x_test)):
	#Actual y value
	actual = y_test[i]
	#Predicted y value
	y_pred = round(predict[i], 2)
	#Test value
	x_precip = x_test[i][0]
	x_winter = x_test[i][1]
	print("Precipitation: ", x_precip, " Winter: ", x_winter, " Predict y val:", y_pred, "Actual y value:", y_test)

plt.tight_layout()
plt.show()