"""
Create a Multiple Lieaner Regression
model to predict the Fawn population
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''Load Data'''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/creatingModel/houses.csv")

'''Create MLR Model'''
x = data[["bathrooms","lot_size_1000_sqft",
	"living_space_1000_sqft","garages",
	"bedrooms","age","num_fire_places"]].values
y = data["selling_price"].values

#Split into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LinearRegression().fit(x_train, y_train)

#Print model info
print("bathrooms coef: ", model.coef_[0])
print("lot size coef: ", model.coef_[1])
print("living space coef: ", model.coef_[2])
print("garages coef: ", model.coef_[3])
print("bedrooms coef: ", model.coef_[4])
print("age coef: ", model.coef_[5])
print("number of fire places coef: ", model.coef_[6])
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
x_bathrooms = x_test[0][0]
x_lot_size = x_test[0][1]
x_living_space = x_test[0][2]
x_garages = x_test[0][3]
x_bedrooms = x_test[0][4]
x_age = x_test[0][5]
x_num_fire_places = x_test[0][6]

print("bathrooms:", x_bathrooms, 
	"lot size:", x_lot_size, 
	"living space size:", x_living_space,
	"garages:", x_garages,
	"bedrooms:", x_bedrooms,
	"age:", x_age,
	"number of fire places:", x_num_fire_places,
	"Predicted price:", predict[0], 
	"Actual house price:", y_test[0])





