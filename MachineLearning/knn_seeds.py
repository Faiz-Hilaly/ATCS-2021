import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

data = pd.read_csv("/Users/faizhilaly/Documents/ATCS-2021/MachineLearning/seeds.csv")
#g = sns.relplot(data=data, x='weather', y='temp', hue = 'outerwear', s=80)
#plt.grid()
#plt.show()

#Read in features and classes
feature_area = data["area"].values
feature_perimeter = data["perimeter"].values
feature_compactness = data["compactness"].values
feature_kernel_length = data["kernel_length"].values
feature_kernel_width = data["kernel_width"].values
feature_asymmetry_coef = data["asymmetry_coef"].values
feature_groove_length = data["groove_length"].values
classes = data['seed'].values

#Set the features to be a 2D array
features = np.array([feature_area, feature_perimeter, feature_compactness, feature_kernel_length, feature_kernel_width, feature_asymmetry_coef, feature_groove_length, feature_groove_length]).transpose()

class_labels = np.unique(data["seed"])

scaler = StandardScaler().fit(features)
features = scaler.transform(features)

features_train, features_test, classes_train, classes_test = train_test_split(features, classes, test_size = 0.2)

#model = KNeighborsClassifier(n_neighbors=5).fit(features_train, classes_train)
#classes_pred = model.predict(features_test)


k_values = []
accuracy = []
for k in range(2, len(classes_train)+1):
# Create a new KNN model with the value k
	model = KNeighborsClassifier(n_neighbors=k).fit(features_train, classes_train)
	classes_pred = model.predict(features_test)
	k_values.append(k)
	accuracy.append(accuracy_score(classes_test, classes_pred))

plt.scatter(k_values, accuracy)
plt.xlabel("k value")
plt.ylabel("Accuracy")
plt.show()


#cm = confusion_matrix(classes_test, classes_pred, labels=class_labels)
#cmd = ConfusionMatrixDisplay(cm, display_labels=class_labels)
#cmd.plot()
#plt.show()
