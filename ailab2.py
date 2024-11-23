import pandas as pd
import numpy as np

# Task 1: Load an Excel Spreadsheet and Print Both Sheets
print("Task 1: Load and Print Sheets")
file_path = '/storage/emulated/0/Download/your_file.xlsx'
xls = pd.ExcelFile(file_path)

# Print all sheet names
print("Sheet Names:", xls.sheet_names)

# Load and print each sheet
for sheet in xls.sheet_names:
    sheet_data = pd.read_excel(xls, sheet_name=sheet)
    print(f"Data from sheet '{sheet}':\n", sheet_data)

# Task 2: Generate a DataFrame with Custom Index and Column Names
print("\nTask 2: Generate Custom DataFrame")
data = {
    'Math': [90, 80, 70, 60, 50],
    'Science': [85, 75, 65, 55, 45],
    'English': [88, 78, 68, 58, 48],
    'History': [92, 82, 72, 62, 52]
}
index_values = ['Ali', 'Amir', 'Kamran', 'Sara', 'Ayesha']

df_custom = pd.DataFrame(data, index=index_values)
print("Generated DataFrame:\n", df_custom)

# Task 3: Read an Excel Spreadsheet and Print the First Two Columns
print("\nTask 3: Print First Two Columns")
df = pd.read_excel(file_path)
print("First Two Columns:\n", df.iloc[:, :2])

# Task 4: Skip the First Two Rows of an Excel Spreadsheet
print("\nTask 4: Skip First Two Rows")
df_skipped = pd.read_excel(file_path, skiprows=2)
print("DataFrame after skipping the first two rows:\n", df_skipped)

# Task 5: Fill Null Values in the "Gender" Column
print("\nTask 5: Fill Null Values in 'Gender' Column")
csv_file_path = '/storage/emulated/0/Download/employees.csv'
df_csv = pd.read_csv(csv_file_path)

# Fill null values in the "Gender" column
df_csv['Gender'] = df_csv['Gender'].fillna('No Gender')

# Print rows from 10 to 30 for visualization
print("DataFrame (Rows 10 to 30):\n", df_csv.iloc[10:31])

# Task 6: Min-Max Normalization for Age and Salary
print("\nTask 6: Min-Max Normalization")
data = {'Age': [20, 30, 40, 50, 60], 'Salary': [2000, 3000, 4000, 5000, 6000]}
df_normalization = pd.DataFrame(data)

df_normalization['Age_Normalized'] = (df_normalization['Age'] - df_normalization['Age'].min()) / (df_normalization['Age'].max() - df_normalization['Age'].min())
df_normalization['Salary_Normalized'] = (df_normalization['Salary'] - df_normalization['Salary'].min()) / (df_normalization['Salary'].max() - df_normalization['Salary'].min())
print("Normalized DataFrame:\n", df_normalization)

# Task 7: Standardization for Age and Salary
print("\nTask 7: Standardization")
df_normalization['Age_Standardized'] = (df_normalization['Age'] - df_normalization['Age'].mean()) / df_normalization['Age'].std()
df_normalization['Salary_Standardized'] = (df_normalization['Salary'] - df_normalization['Salary'].mean()) / df_normalization['Salary'].std()
print("Standardized DataFrame:\n", df_normalization)

# Task 8: Interpolate Missing Values Using Backward Interpolation
print("\nTask 8: Backward Interpolation")
# Create the DataFrame
data = {
    'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score': [np.nan, 40, 80, 98],
}
df = pd.DataFrame(data)

# Perform backward fill for missing values
df = df.bfill()

print("DataFrame after Backward Interpolation:\n", df)