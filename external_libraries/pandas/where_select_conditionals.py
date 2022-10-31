import pandas as pd

df_titanic = pd.read_csv('../../support/titanic_data.csv')  # create a DataFrame from a CSV

# SELECT some rows depending on a specific condition
# (WHERE) in Dataframes

# WHERE to a single column
# df['column1'] condition
age_filter = df_titanic["Age"] > 35  # returns a Series with all the coincidences

print(
    df_titanic[age_filter]  # uses the Series to filter the original DataFrame
)  # It returns a new filtered DataFrame

# Creates a Series filter which is uses to create a new filtered DataFrame
# df[df['column'] condition = Filter Series]
above_35 = df_titanic[df_titanic["Age"] > 35].tail(9)
print('WHERE of a single column: \nAbove 35:')
print(
    above_35
)

# WHERE with more than a single condition to the same column
# Every conditional operation must be surrounded by ( )
# And followed by a Logical Operator
# df[    (df["column_name"] condition)  &  (df["column_name"] condition)   ]
# df[    (df["column_name"] condition)  |  (df["column_name"] condition)   ]
between_35_and_40 = df_titanic[(df_titanic["Age"] > 35) & (df_titanic["Age"] < 40)]

print('Titanic passengers between 35 and 40 years:')
print(between_35_and_40.shape)

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

# WHERE to more than a column

# df[    (df["column1"] condition)  &  (df["Column2"] condition)   ]
# df[    (df["column1"] condition)  |  (df["Column2"] condition)   ]
above_35_and_passenger_id_860 = df_titanic[(df_titanic["Age"] > 35) & (df_titanic["PassengerId"] > 860)].tail(9)

print(df_titanic.dtypes)

print(
    df_titanic["Age"] > 35
)


# df.loc attribute
# Allows to apply a filter and specify which columns will be returned

# Specifying a single column in the returned DataFrame
passengers_33_years_name = df_titanic.loc[df_titanic['Age'] == 33, 'Name']
print("Passenger's name & Id:")
print(passengers_33_years_name)


# Specifying more than a column in the returned DataFrame
passengers_33_years_info = df_titanic.loc[df_titanic['Age'] == 33, ['Name', 'PassengerId']]

print("Passenger's name & Id:")
print(passengers_33_years_info)
