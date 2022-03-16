'''Creates a Logistic Regression Model  to determine if someone will buy an SUV'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

'''Load Data'''
data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/creatingModel/diamonds.csv")

# Replace qualitative data with quantitative
data["cut"].replace(["Premium", "Fair"], [0, 1], inplace=True)

x = data[["carat", "depth", "table"]].values
y = data["cut"].values

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

# scale the inputs
x_pred = [[carat, depth, table]]
x_pred = scaler.transform(x_pred)

# make and print prediction
if model.predict(x_pred)[0] == 1:
    print("Fair")
else:
    print("Premium")