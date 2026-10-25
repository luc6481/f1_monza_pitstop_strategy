'''
adding extension rf
Lucia Lindow
9-24-26
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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
X = monza_data.iloc[:, [6, 7, 8, 10]].values

num_pitstops = monza_data.iloc[:, [1]]
pitstop1 = monza_data.iloc[:, [2]]
pitstop2 = monza_data.iloc[:, [3]]
pitstop3 = monza_data.iloc[:, [4]]


y = np.column_stack([num_pitstops,pitstop1, pitstop2, pitstop3])

#splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

#scaling features -- I believe this scales all of the features similarly
scaler = StandardScaler()
#print(y_train)
X_train = scaler.fit_transform(X_train)

X_test2 = X_test[:, [0,1,2]]
##print(X_test2)
for i in range(len(X_test2)):
    X_test2[i, 1] = 'NaN' #y_test[i, 0] - 1
    X_test2[i, 2] = 'NaN'
    #X_test2[i, 3] = 'NaN'
#print(X_test2)
X_test = scaler.transform(X_test)
X_test2 = scaler.transform(X_test2)
#print(X_test2)

#building the Random Forest Classifier
classifier = RandomForestClassifier(n_estimators= 10, random_state=8) #n_estimators is number of trees
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test2) #predicting the test data


#evaluating the model
#accuracy = accuracy_score(y_test, y_pred)
#print(f'Accuracy: {accuracy * 100:.2f}%')

#conf_matrix = confusion_matrix(y_test, y_pred)
#print(y_pred)
#print(y_test)
counter_col0_same = 0
counter_col1_same = 0
counter_col2_same = 0
counter_col3_same = 0

counter_col0_wi5 = 0
counter_col1_wi5 = 0
counter_col2_wi5 = 0
counter_col3_wi5 = 0

for i in range(len(y_pred)):
    if y_pred[i, 0] == y_test[i, 0]:
        counter_col0_same +=1
    elif abs(y_pred[i, 0] - y_test[i,0]) <= 5:
        counter_col0_wi5 += 1

    if y_pred[i, 1] == y_test[i, 1]:
        counter_col1_same +=1
    elif abs(y_pred[i, 1] - y_test[i,1]) <= 5:
        counter_col1_wi5 += 1

    if y_pred[i, 2] == y_test[i, 2]:
        counter_col2_same +=1
    elif abs(y_pred[i, 2] - y_test[i,2]) <= 5:
        counter_col2_wi5 += 1

    if y_pred[i, 3] == y_test[i, 3]:
        counter_col3_same +=1
    elif abs(y_pred[i, 3] - y_test[i,3]) <= 5:
        counter_col3_wi5 += 1

print("Col 0 exact accuracy:" , counter_col0_same , "\n Col 0 wi 5 accuracy:" , counter_col0_wi5)
print("Col 1 exact accuracy:" , counter_col1_same , "\n Col 1 wi 5 accuracy:" , counter_col1_wi5)
print("Col 2 exact accuracy:" , counter_col2_same , "\n Col 2 wi 5 accuracy:" , counter_col2_wi5)
print("Col 3 exact accuracy:" , counter_col3_same , "\n Col 3 wi 5 accuracy:" , counter_col3_wi5)


feature_importances = classifier.feature_importances_
print(feature_importances)
