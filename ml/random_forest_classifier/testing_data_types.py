'''
Testing data in RF
Lucia Lindow
9-24-26
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier


monza_data = pd.read_csv("C:/Users/Lucia/OneDrive - Culver Educational Foundation/in CS/datasets/final_data.csv")
monza_data = pd.DataFrame(monza_data)

#printing the dataset to see what it looks like
print(monza_data.head())

#separate the features with from the target variable
#taking all rows and every column but the last
X = monza_data.iloc[:, [1, 2, 3, 4, 6, 8, 9, 10]].values

#taking all rows and only the last column
y = monza_data.iloc[:, 7].values

#splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

#scaling features -- I believe this scales all of the features similarly
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#building the Random Forest Classifier
classifier = RandomForestClassifier(n_estimators= 100, random_state=8) #n_estimators is number of trees
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test) #predicting the test data


#evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

conf_matrix = confusion_matrix(y_test, y_pred)
print(y_pred)
print(y_test)
plt.figure(figsize=(8, 6))
#sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', cbar=False, 
            #xticklabels=monza_data.ChangeInPosition_names, yticklabels=monza_data.ChangeInPosition_names)

#plt.title('Confusion Matrix Heatmap')
#plt.xlabel('Predicted Labels')
#plt.ylabel('True Labels')
#plt.show()

#showing the feature importance
feature_importances = classifier.feature_importances_
print(feature_importances)
#plt.barh(monza_data.feature_names, feature_importances)
#plt.xlabel('Feature Importance')
#plt.title('Feature Importance in Random Forest Classifier')
#plt.show()
