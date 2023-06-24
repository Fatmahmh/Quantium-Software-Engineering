import pandas as pd


import pandas as pd

# Read the three data files into separate DataFrames
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Merge the three DataFrames into a single DataFrame
data = pd.concat([df0, df1, df2], ignore_index=True)

# Print the first few rows of the merged DataFrame to verify the result
print(data.head())

# Drop any row that doesn't have "Pink Morsels" in the "product" column
data = data[data['product'] == 'pink morsel']

# Remove the dollar sign from the "price" column and convert to numeric
data['price'] = data['price'].str.replace('$', '').astype(float)

# Create a new column called "sales" by multiplying "quantity" and "price"
data['sales'] = data['quantity'] * data['price']

# Drop all columns except "Sales", "Date", and "Region"
data = data[['sales', 'date', 'region']]

# Export the modified data to a new CSV file
data.to_csv('modified_data.csv', index=False)