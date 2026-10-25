import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

warnings.filterwarnings('ignore')

monza_data = pd.read_csv("CHANGE_ME")
monza_data = pd.DataFrame(monza_data)

#separate the features with from the target variable
#taking all rows and every column but the last
X = monza_data.iloc[:, [1, 2, 3, 4, 6, 8, 9, 10]].values

#taking all rows and only the last column
y = monza_data.iloc[:, 7].values

label_encoder = LabelEncoder()

for col in monza_data.select_dtypes(include=['object']).columns:
    monza_data[col] = label_encoder.fit_transform(monza_data[col])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)

regressor = RandomForestRegressor(n_estimators=15, random_state=8, oob_score=True)

regressor.fit(X_train, y_train)



print("Out-of-Bag Score:", regressor.oob_score_)

y_pred = regressor.predict(X_test)
for i in range(len(y_pred)):
    y_pred[i] = y_pred[i].round(0)
    if y_pred[i] == -0:
        y_pred[i] = 0
print(y_pred)
print(y_test)

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)

r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
