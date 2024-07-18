#%% 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. Load the dataset into a pandas dataframe.
df = pd.read_csv('cereal.csv')

#%%
#2. Print the first 5 rows of the dataset.
print(df.head())
print('\n')

#%%
#3. Use pandas to generate a description of the dataset.
print(df.describe())
print('\n')

#%%
#4. Print the correlation matrix of the dataset. 
#Which two columns have the highest correlation & which two columns have the lowest correlation? 
#Generate a correlation matrix plot using pandas.

numeric_df = df.select_dtypes(include=[np.number])

correlation_matrix = numeric_df.corr()
print(correlation_matrix)
print('\n')

highest_corr = correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates()
lowest_corr = correlation_matrix.unstack().sort_values().drop_duplicates()

print(f'Highest correlation: {highest_corr.index[1]} -> {highest_corr.iloc[1]}')
print(f'Lowest correlation: {lowest_corr.index[0]} -> {lowest_corr.iloc[0]}')
print('\n')

plt.figure()
cax = plt.matshow(correlation_matrix, cmap='coolwarm')
plt.colorbar(cax)
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix', pad=20)
plt.show()

#%%
#5. Use pandas to plot a scatter matrix of the dataset.
pd.plotting.scatter_matrix(numeric_df, figsize=(15, 15), diagonal='hist')
plt.show()

#%%
#6. Create a bar chart of the number of cereals in each manufacturer

manufacturer_counts = df['mfr'].value_counts()
plt.figure(figsize=(10, 6))
manufacturer_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Cereals per Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

#%%
#7. Generate a scatter plot of the calories vs. the rating of the cereal
plt.figure(figsize=(10, 6))
plt.scatter(df['calories'], df['rating'], color='purple')
plt.title('Calories vs. Rating')
plt.xlabel('Calories')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

#%%
#8. Select a few interesting looking graphs from the scatter matrix generated in problem 6 
# make them visually appealing
plt.figure(figsize=(10, 6))
plt.scatter(df['calories'], df['sugars'], color='blue')
plt.title('Calories vs. Sugars')
plt.xlabel('Calories')
plt.ylabel('Sugars')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['fiber'], df['rating'], color='green')
plt.title('Fiber vs. Rating')
plt.xlabel('Fiber')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['sugars'], df['rating'], color='green')
plt.title('Sugars vs. Rating')
plt.xlabel('Sugars')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

#%%
#9.Create a histogram of the ratings of the cereals
plt.figure(figsize=(10, 6))
df['rating'].plot(kind='hist', bins=20, color='orange', edgecolor='black')
plt.title('Histogram of Cereal Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#%%
#10. Describe any conclusions you can make about the dataset.
conclusions = """
1. The more calories there are, the lower the rating tends to be. Same goes for sugar. 
2. Potassium and fiber have a strong positive correlation.
3. The average cereal rating was in the upper 30s.
"""
print(conclusions)
# %%
