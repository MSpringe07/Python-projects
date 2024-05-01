# Data Analysis and Processing Scripts

These Python scripts perform various data analysis and processing tasks using the pandas library.

## Features

1. The first script reads data from a CSV file, identifies missing values, removes duplicate rows, replaces numbers with words, deletes a column, removes rows containing missing values, and creates a scatter plot.
2. The second script reads data from an Excel file, calculates new columns, saves data to an Excel file, groups data by a column, filters data based on a condition, and saves the results to separate sheets in an Excel file.

## How to Run

You can run these scripts using Python 3. Make sure you have the `pandas` and `matplotlib.pyplot` libraries installed. If not, you can install them using pip:

\`\`\`bash
pip install pandas matplotlib
\`\`\`

Then, you can run the scripts:

\`\`\`bash
python script_name.py
\`\`\`

Replace `script_name.py` with the name of the script file.

## Input

The scripts expect CSV and Excel files in the same directory. The names of the files are 'auto_imports_mainits.csv' and 'dati_masiviem_og.xlsx', respectively.

## Output

The first script prints the number of missing values in each column, the size of the table before and after removing duplicates, and the number of missing values in each column after deleting a column. It also displays a scatter plot.

The second script saves the processed data to an Excel file. It also prints the total money, total books, and total profit. It saves the grouped and filtered data to separate sheets in the Excel file.

## Note

The scripts use the pandas library to perform data analysis and processing tasks. The first script also uses the matplotlib.pyplot library to create a scatter plot. The second script uses the openpyxl engine to write data to an Excel file.
