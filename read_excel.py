#----------------------------------------------------------------------------------
# File Path: /Users/gb105/OneDrive/Documents/GitHub/nbk5876.github.io/breeds.xlsx
#----------------------------------------------------------------------------------
import pandas as pd

# Specify the path of your Excel file
file_path = 'C:/Users/gb105/OneDrive/Documents/GitHub/nbk5876.github.io/breeds.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
print(df.head(20))
