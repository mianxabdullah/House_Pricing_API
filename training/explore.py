from sklearn.datasets import fetch_california_housing
import pandas as pd

def load_california_housing():
    housing_data = fetch_california_housing(as_frame=True)   # as_frame=True returns a pandas DataFrame instead of a NumPy array
    df = housing_data.frame     # Convert to DataFrame
    return df

data=load_california_housing()

#Explore the data
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(data.dtypes)

data.to_csv('california_housing.csv', index=False)  # Save the DataFrame to a CSV file