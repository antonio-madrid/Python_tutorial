import pandas as pd

df_titanic = pd.read_csv('../../support/titanic_data.csv')  # create a DataFrame from a CSV

# ------------------------------------------------------------------------------------------------------
# DataFrame's conditionals filters
# ------------------------------------------------------------------------------------------------------

# SELECT some rows depending on a specific condition
# (SQL WHERE) in Dataframes

# ------------------------------------------------------------------------------------------------------
# One single filter (SQL WHERE)
# ------------------------------------------------------------------------------------------------------

# Applying a filter to a single column
# df['column1'] condition
age_filter = df_titanic["Age"] > 35  # returns a Series with all the coincidences

print('Passengers above 35 years:')
print(
    df_titanic[age_filter]  # uses the Series to filter the original DataFrame
)  # It returns a new filtered DataFrame


# Applying a filter to a single column where accessing the column as an object attribute
sex_filter = df_titanic.Sex == 'female'  # Accessing the column as an Object attribute
print('Female passengers:')
print(
    df_titanic.Name[sex_filter]  # This returns a new DataFrame with a single column, Name, and applies a filter on it
)


# SQL:                                   SELECT column_name FROM dataframe_name WHERE condition
# Pandas is a reversed SQL sentence:     FROM dataframe_name SELECT column_name WHERE condition
# But in Pandas is:                      dataframe_name[filter_series condition]

# Creates a Series filter which is uses to create a new filtered DataFrame
# df[df['column'] condition = Filter Series]
above_35 = df_titanic[df_titanic["Age"] > 35].tail(9)
print('WHERE of a single column: \nAbove 35:')
print(
    above_35
)


# ------------------------------------------------------------------------------------------------------
# More than a filter
# ------------------------------------------------------------------------------------------------------


# SQL WHERE with more than a single condition to the same column
# Every conditional operation must be surrounded by ( )
# And followed by a Logical Operator
# df[    (df["column_name"] condition)  &  (df["column_name"] condition)   ]
# df[    (df["column_name"] condition)  |  (df["column_name"] condition)   ]
between_35_and_40 = df_titanic[(df_titanic["Age"] > 35) & (df_titanic["Age"] < 40)]

print('Titanic passengers between 35 and 40 years:')
print(between_35_and_40.shape)


# SQL WHERE to multiples columns
# df[    (df["column1"] condition)  &  (df["Column2"] condition)   ]
# df[    (df["column1"] condition)  |  (df["Column2"] condition)   ]
above_35_and_passenger_id_860 = df_titanic[(df_titanic["Age"] > 35) & (df_titanic["PassengerId"] > 860)].tail(9)

# Specifying more than a column or more than a condition to the same columns is written pretty much the same
print(f'Titanic passengers above 35 years old and above passenger id 860: {above_35_and_passenger_id_860}')


# ------------------------------------------------------------------------------------------------------
# Conditionals as functions
# ------------------------------------------------------------------------------------------------------

# between()
# Apply a filter between a range, it is the same operation as the last one
between_35_and_40 = df_titanic[df_titanic["Age"].between(35, 40, inclusive="neither")]
# inclusive determines to include the extreme numbers in the operations

print('Titanic passengers between 35 and 40 years by between() function:')
print(between_35_and_40.shape)


# isin() - Filters the DataFrame by the given value
# df[       df['column_name'].isin( [ comparable_value1, comparable_value2 ] )      ]
passengers_33_years = df_titanic[df_titanic["Age"].isin([33, 34])]  # All the conditions must be given as a list
print('33 years old passengers by isin() function:')
print(
    passengers_33_years
)

#  This code does the same as isin() function
passengers_33_years = df_titanic[(df_titanic["Age"] == 33) | (df_titanic["Age"] == 34)]
print('33 years old passengers:')
print(
    passengers_33_years
)


# ------------------------------------------------------------------------------------------------------
# df.loc attribute - rows and columns LOCators
# ------------------------------------------------------------------------------------------------------

# SELECT rows and columnS of a DataFrame
# df.loc[rows, columns]

# Rows and Columns can be SELECTed by its label, condition (filter)

# Specifying a single column in the returned DataFrame
passengers_33_years_name = df_titanic.loc[df_titanic['Age'] == 33, 'Name']  # Just selecting column 'Name' (label)
# Allows to apply a filter and specify which columns will be returned by its labels
print(f"Passenger's name & Id: {passengers_33_years_name}")


# Specifying more than a column in the returned DataFrame
passengers_33_years_info = df_titanic.loc[
    df_titanic['Age'] == 33, ['Name', 'PassengerId']  # Selecting columns 'Name' and 'PassengerId' (labels)
]

print(f"Passenger's name & Id: {passengers_33_years_info}")

# loc creates a subset (new filtered DataFrame)


# ------------------------------------------------------------------------------------------------------
# iloc - Integer LOCators
# ------------------------------------------------------------------------------------------------------

# Similar to loc but accessing to Rows or Columns by its Integer position
# Pandas indexes every row and column by default assigning a number

# Structure:
# df.iloc[rows_index_range, columns_index_range]

# SELECTing columns: Name, Sex, Age and rows from 25 to 35
ten_passengers_info = df_titanic.iloc[25:35, 3:5]  # Name, Sex, Age positions = 3:5

print(f'Passengers info from 25 to 35 in the list: {ten_passengers_info}')

# iloc is the perfect solution when knowing the index number of the rows actually wanted
