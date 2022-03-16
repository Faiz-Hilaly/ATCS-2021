'''Creates a Logistic Regression Model  to determine if someone will buy an SUV'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

'''Load Data'''
data = pd.read_csv("../Data/suv.csv")

# Replace qualitative data with quantitative
data["Gender"].replace(["Male", "Female"], [0, 1], inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Scale data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Split into train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

'''Create Model'''
model = LogisticRegression().fit(x_train, y_train)

# Print model info
coef = model.coef_[0]
print("Weights for model:")
print(coef)
print()

# Get confusion matrix
y_pred = model.predict(x_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print()

print("Accurary", model.score(x_test, y_test))

# Make a new prediction
age = int(input("How old is the customer?\n"))
gender = int(input("Is the customer Male (0) or Female (1)?\n"))
salary = int(input("How much does the customer make in a year?\n"))

# scale the inputs
x_pred = [[age, salary, gender]]
x_pred = scaler.transform(x_pred)

# make and print prediction
if model.predict(x_pred)[0] == 1:
    print("This customer will buy an SUV.")
else:
    print("This customer will not buy an SUV.")