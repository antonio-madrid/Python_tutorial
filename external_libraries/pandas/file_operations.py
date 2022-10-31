import pandas as pd

# ------------------------------------------------------------------------------------------------------
# Read & write data with Pandas
# ------------------------------------------------------------------------------------------------------

df_titanic = None

# pd.read_csv() creates a DataFrame from the given csv
try:  # Reading external data can cause errors
    df_titanic = pd.read_csv('../../support/titanic_data.csv')
except Exception:
    print('File not found or File corrupted.')

if df_titanic is not None:
    print(
        df_titanic
    )

# Export a DataFrame to other type such as Excel or CSV
df_titanic.to_excel('../../support/titanic_data.xlsx', sheet_name='passengers', index=False)

# .to_excel, to_csv etc requires the new file path + name
# the sheet name in the case of an Excel file
# and index indicates if we would to include the extra column that Pandas create to identify each row by a number
df_titanic.to_csv('../../support/titanic_data_backup.csv', index=False)  # CSVs do not have sheet_name

# Import a DataFrame from an Excel
df_titanic_from_excel = pd.read_excel('../../support/titanic_data.xlsx', sheet_name='passengers')
