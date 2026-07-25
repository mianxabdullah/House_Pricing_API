from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import pandas as pd

data = pd.read_csv('california_housing.csv')

X = data.drop('MedHouseVal', axis=1) 
y = data['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"average mean squared error: ${mse *100000:,.0f}")
print(f"R-squared: {r2:.4f}")

joblib.dump(model, 'house_model.joblib')  
joblib.dump(list(X.columns), 'house_features.joblib') # save the feature names for later use

