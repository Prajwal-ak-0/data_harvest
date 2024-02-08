import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Load the data
data = pd.read_csv('Data2.csv')

X = data.drop('Rating', axis=1)
y = data['Rating']

numeric_cols = X.select_dtypes(include=np.number).columns
X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].median())

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc_X = StandardScaler()
X_train_scaled = sc_X.fit_transform(X_train)
X_test_scaled = sc_X.transform(X_test)

regressor = SVR(kernel='rbf')
regressor.fit(X_train_scaled, y_train)

y_pred = regressor.predict(X_test_scaled)

new_data = [[20, 0, 1, 0, 0, 0, 0, 0, 0, 0]]

new_pred = regressor.predict(new_data)

print("The predicted rating is:", new_pred[0])