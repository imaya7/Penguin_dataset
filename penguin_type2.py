import pandas as pd

# Ensure the file path includes the file extension
# This code is to figure out the number of unique species and islands in the dataset
try:
	data = pd.read_excel(r'C:\Users\trash\Downloads\penguin_size.xlsx')
except FileNotFoundError:
	print("The file was not found. Please check the file path.")
	data = pd.DataFrame()  # Create an empty DataFrame to avoid further errors

# Display the first few rows of the dataset
print(data.head())

# Count the number of unique species
unique_species = data['species'].nunique()
print(f"Number of unique species: {unique_species}")

# Count the number of unique regions
unique_island = data['island'].nunique()
print(f"Number of unique island: {unique_island}")