import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

''' Load Data '''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/breast_cancer.csv")

# Reload and/or reformat the data to get the values from x and y
x = data[["Age", "Nodes"]].values
y = data["Survived_5_Years"].values

# Scale data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

# Separate data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create multivariable linear regression model
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
age = int(input("How old is the patient?\n"))
nodes = int(input("What is the patient's number of detected axillary nodes?\n"))

# scale the inputs
x_pred = [[age, nodes]]
x_pred = scaler.transform(x_pred)

# make and print prediction
if model.predict(x_pred)[0] == 1:
    print("This patient will survive 5 years or longer.")
else:
    print("Dead within 5 years.")