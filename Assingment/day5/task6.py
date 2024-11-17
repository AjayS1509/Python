import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

data1 = { 'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1], 'C': [2, 3, 4, 5, 6], 'D': [5, 6, 7, 8, 9] }
df=pd.DataFrame(data1)
df.to_csv("sample_data.csv",index=False)
corr_matrix=df.corr()

# Plot the heatmap of the correlation matrix using seaborn
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',linewidths=0.5)
plt.title('Correaltion Heatmap')
plt.show()

# Plot the scatter plot for the two highest correlated columns using matplotlib and plotly  Find the two highest correlated columns
corr_pairs=corr_matrix.unstack()
sorted_pairs=corr_pairs.sort_values(kind="quicksort",ascending=False)
highest_corr=sorted_pairs[1:2]
col1,col2=highest_corr.index[0]

# Scatter plot using matplotlib
plt.figure(figsize=(8,6))
plt.scatter(df[col1],df[col2],alpha=0.5)
plt.title(f'Scatter Plot of {col1} vs {col2}')
plt.xlabel(col1)
plt.ylabel(col2)
plt.show()