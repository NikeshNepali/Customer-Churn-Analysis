# Importing the panda model
import pandas as pd 

# Reading the Csv file
csv_file = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.Csv")

# Display of Results
print(csv_file.head())

# Storing whole file in one single dataframe
df = pd.DataFrame(csv_file)

# Cleaning the datasets.
print(df.dtypes)
print(df)

# Checking the empty Columns and missing values
missingValues = df.isna().sum()
print(missingValues)

# Removing the given churn
df = df.drop(columns=['Churn'])
# Adding a new colum using tenure to get the churn
# using lambda function if tenure is less tehn 10 then it is churn.
df['Churn'] = df['tenure'].apply(lambda a: 'Yes' if a > 10 else 'No')

# Cleaned Dataset
print(df)
