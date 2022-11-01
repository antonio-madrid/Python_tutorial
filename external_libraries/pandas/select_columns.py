import pandas as pd

df_titanic = pd.read_csv('../../support/titanic_data.csv')  # create a DataFrame from a CSV

# ------------------------------------------------------------------------------------------------------
# SELECT DataFrame's columns
# ------------------------------------------------------------------------------------------------------

#  SELECT specific columns of a DataFrame
# It is the same as SQL, to SELECT just type the column name as a dictionary


# ------------------------------------------------------------------------------------------------------
# SELECT one_column
# ------------------------------------------------------------------------------------------------------

print('SELECT Name FROM df_titanic')
print(
    df_titanic['Name'].tail(9)  # Only gets one column and all its values
)  # When SELECTing a single column, its column name does not appear


# SELECT one column as an object attribute
print('SELECT Ticket FROM df_titanic')
print(
    df_titanic.Ticket.tail(9)
)


# SQL:                                   SELECT column_name FROM dataframe_name
# Pandas is a reversed SQL sentence:     FROM dataframe_name SELECT column_name
# But in Pandas is:                      dataframe_name['column_name']


# ------------------------------------------------------------------------------------------------------
# SELECT multiple_columns
# ------------------------------------------------------------------------------------------------------

print('SELECT Name, Sex, Age FROM df_titanic')
print(  # SELECT more than one column
    df_titanic[['Name', 'Sex', 'Age']].tail(9)  # To select multiple columns, use a list
)

# These operations always returns a new DataFrame
print('SELECT returned type:')
print(
    type(df_titanic[['Name', 'Sex', 'Age']].tail(9))
)


# ------------------------------------------------------------------------------------------------------
# Column's shape
# ------------------------------------------------------------------------------------------------------

# df['one_column'].shape
# It returns the number of rows when applying to a single column

print('df["one_column"].shape:')
print(
    df_titanic['Name'].shape  # When calling a single column just the number of rows are returned
)

print('df["one_column", "another_column"].shape:')
print(
    df_titanic[['Name', 'Age', 'Sex']].shape  # Counts the number of rows & columns
)

