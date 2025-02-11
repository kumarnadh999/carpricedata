import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv('cleaned_data.csv')

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Plotting graphs for data analysis

# Distribution of car prices
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, bins=30)
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('car_price_distribution.png')
plt.show()

# Scatter plot of Price vs. Year
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='Price', data=df)
plt.title('Price vs. Year')
plt.xlabel('Year')
plt.ylabel('Price')
plt.savefig('price_vs_year.png')
plt.show()

# Scatter plot of Price vs. Kilometers Driven
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Kilometers_Driven', y='Price', data=df)
plt.title('Price vs. Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.savefig('price_vs_kilometers_driven.png')
plt.show()

# Box plot of Price by Fuel Type
plt.figure(figsize=(10, 6))
sns.boxplot(x='Fuel_Type', y='Price', data=df)
plt.title('Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.savefig('price_by_fuel_type.png')
plt.show()

# Box plot of Price by Transmission Type
plt.figure(figsize=(10, 6))
sns.boxplot(x='Transmission', y='Price', data=df)
plt.title('Price by Transmission Type')
plt.xlabel('Transmission Type')
plt.ylabel('Price')
plt.savefig('price_by_transmission_type.png')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.show()
