import pandas as pd

df_titanic = pd.read_csv('../../support/titanic_data.csv')  # create a DataFrame from a CSV

# ------------------------------------------------------------------------------------------------------
# UPDATE
# ------------------------------------------------------------------------------------------------------

# UPDATing/modifying data of DataFrame's rows

# To perform any update, SELECT which rows and which column of those rows are going to be modified


# ------------------------------------------------------------------------------------------------------
# iloc
# ------------------------------------------------------------------------------------------------------

# When SELECTing rows with iloc, a new value can be assigned to those rows column
names = df_titanic.iloc[0:3, 3] = 'anonymous'

print(names)
