# Write a NumPy program to convert Pandas dataframe to Numpy array with
# headers.

import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Convert DataFrame to NumPy array
numpy_array = df.to_numpy()

# Get headers
headers = df.columns.to_numpy()

# Combine headers and data
result = np.vstack([headers, numpy_array])

print("NumPy array with headers:")
print(result)