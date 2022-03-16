import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/chirping.csv")

x = data["Temp"].values
y = data["Chirps"].values

#Seperate data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Reshape x to a 2D array
x_train = x_train.reshape(-1,1)
print(x)

#Create the Model
model = LinearRegression().fit(x_train, y_train)

#Find the slope, bias, and r squared values
slope = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x_train, y_train)

#Test model
#x_predict = 77
#prediction = model.predict([[x_predict]])

#Reshape test data into 2d array
x_test = x_test.reshape(-1,1)

#Get the predicted y values for the x_test values
predict  = model.predict(x_test)

#Compare the actual and predicted values
print("Testing Linear Model with Test Data: ")
for i in range(len(x_test)):
	#Actual y value
	actual = y_test[i]
	#Predicted y value
	y_pred = round(predict[i], 2)
	#Test value
	x_val = x_test[i]
	print("x val:", float(x_val), " Predict y val:", y_pred, "Actual y value:", y_test)

#Print results
print("Linear Equation: y =", slope, "x +", intercept)
print("R Squared = ", r_squared)
#print("Prediction when x is", x_predict, " = ", prediction)

#Visualize Linear Regression
plt.figure(figsize=(5, 4))

plt.scatter(x_train, y_train, c="purple", label="Trainging Data")
plt.scatter(x_test, y_test, c="blue", label="Testing Data")
plt.scatter(x_test, predict, c="green", label="Predictions")

plt.xlabel("Temp")
plt.ylabel("Chirps/min")
plt.title("Cricket Chirps in Temps")
plt.plot(x,slope*x + intercept, c="red", label="Line of best fit")

plt.legend()
plt.show()
