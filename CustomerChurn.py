# Importing the panda model
import pandas as pd 
# Importing the matplot library for visualization
import matplotlib.pyplot as plt 

# Reading the Csv file
csv_file = pd.read_csv("https://github.com/NikeshNepali/Customer-Churn-Analysis/raw/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")

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

print(df.describe())


# Plotting the datasets
gender_Counts = df['gender'].value_counts()
# Unstacked bar chart.
ax = gender_Counts.plot(kind='bar',color = ['lightblue','purple'])


# Labelling the bar chart
for i, gender in enumerate(gender_Counts):
    ax.text(i,
            gender + 1,
            str(gender),
            ha = "center",
            va = "bottom")
    
plt.title("Gender Counts in Total")
plt.xlabel("Male/Female")
plt.ylabel("Total # of Gender")
plt.tight_layout()

# Stacked Bar chart.
churn__gender_counts = df.groupby(['gender','Churn']).size().unstack(fill_value = 0)
# Using ax variable for reference to further use this to label.
ax = churn__gender_counts.plot(kind='bar', stacked= True, color =['red','blue'])

# Labelling at the middle of the barchart.
for i, gender in enumerate(churn__gender_counts.index):
    total_height = 0
    # Nested for loop for getting the height and count of each innere gender and churn.
    for churn in churn__gender_counts.columns:
        # getting the height using the .loc method it calculates the total.
        height = churn__gender_counts.loc[gender, churn] 
        # Only labeling when height is greater then 0.
        if height > 0:
            ax.text(i, total_height + height/2,str(height), ha = "center", va = "center", fontsize = 10, color = 'black')


# display of results.
plt.title('Gender Count')
plt.xlabel('Gender')
plt.ylabel('Gender & Churn Count')
plt.xticks(rotation = 0)

# Creating a Pie Chart.
plt.figure(figsize=(8,6))
churnss = df['Churn'].value_counts()
plt.pie(churnss, # the datas that are being evaluated.
        labels= churnss.index, # Labels of the percentage data
        autopct='%1.1f%%',# Helps get the percentage
        colors= ['red', 'yellow'],
        startangle=90)
plt.title("Gender Distribution")
plt.axis('Equal')

# Creating a Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(df['MonthlyCharges'],df['tenure'], color = 'red', marker= 'o')
plt.title('Tenure and Monthly Charge')
plt.xlabel('monthlycharge')
plt.ylabel('tenure')
plt.tight_layout()

plt.show()
