import pandas as pd
import matplotlib.pyplot as plt

# Read the data
dati = pd.read_csv('auto_imports_mainits.csv')

# Identify missing values
missing_values = dati.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Output table size
print("Table size before removing duplicates: ", dati.shape)

# Count duplicate rows
print("Number of duplicate rows: ", dati.duplicated().sum())

# Remove duplicate rows
dati = dati.drop_duplicates()
print("Table size after removing duplicates: ", dati.shape)

# Replace verbal numbers with actual numbers
num_to_word = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve"
    # Add more if needed
}

# Replace numbers with words
for num, word in num_to_word.items():
    dati = dati.replace(num, word)
# Output 3 example rows
print(dati.sample(3))

# Delete the 'normalized-losses' column
del dati['normalized-losses']

# Recount the number of voids
missing_values = dati.isnull().sum()
print("Missing values in each column after deleting 'normalized-losses':\n", missing_values)

# Delete rows containing missing values
dati = dati.dropna()

# Re-output table size
print("Table size after removing rows with missing values: ", dati.shape)

# Create a scatter plot for 'engine-size' and 'price'
dati.plot.scatter('engine-size', 'price')

# Display the plot
plt.show()











