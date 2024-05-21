import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('customer_data.csv')

# Display the first few rows, summary statistics, and info about the dataset
print(df.head())
print(df.describe())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing values in 'Total Charges' with the mean
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df['Total Charges'].fillna(df['Total Charges'].mean(), inplace=True)

# Drop rows with missing 'Churn Reason'
df.dropna(subset=['Churn Reason'], inplace=True)

# Drop irrelevant columns
df.drop(columns=['CustomerID', 'Country', 'State', 'City', 'Zip Code', 'Lat Long', 'Count'], inplace=True, errors='ignore')

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 
                                         'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 
                                         'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies', 
                                         'Contract', 'Paperless Billing', 'Payment Method', 'Churn Label', 
                                         'Churn Reason'])

# Standardize numerical columns
scaler = StandardScaler()
numerical_columns = ['Tenure Months', 'Monthly Charges', 'Total Charges', 'Churn Score', 'CLTV']
df_encoded[numerical_columns] = scaler.fit_transform(df_encoded[numerical_columns])

# Save the cleaned dataset
df_encoded.to_csv('cleaned_customer_data.csv', index=False)
