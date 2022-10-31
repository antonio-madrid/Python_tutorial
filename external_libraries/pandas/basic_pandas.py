# ------------------------------------------------------------------------------------------------------
# Pandas
# ------------------------------------------------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------------------------------------------------
# Dataframes
# ------------------------------------------------------------------------------------------------------
# Dataframes represents a table like a SQL or Excel table

# Simple DataFrame
df = pd.DataFrame(
    {
        'Column1': [
            'value1',
            'value2',
            'value3'
        ],
        'Column2': ''
    }
)
# DataFrame constructor allows to create a Dataframe, it needs a dictionary as input
# DataFrame Structure = Dictionary of: Column name : List of row values
df_people = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df_people)

df_animals = pd.DataFrame(
    {
        'num_legs': [2, 4],
        'num_wings': [2, 0]
    },
    index=['falcon', 'dog'])  # Index allows to modify the Index column names instead of the numbered default one

print(df_animals)

# Dataframe must be a dictionary of: Column name + List of values
df_person = pd.DataFrame(
    {
        'name': ['Antonio'],
        'age': [33],
        # Inserting an object instead a list results in an error
        # 'id': {
        #     'number': [12345678],
        #     'expire_date': ['22-02-2024']
        # }
        # The only way to work around this is inserting object in a list
        'id': [
            {
                'number': [12345678],
                'expire_date': ['22-02-2024']
            }
        ]
    }
)

print(df_person)

# ------------------------------------------------------------------------------------------------------
# DataFrame operations
# ------------------------------------------------------------------------------------------------------

df_titanic = pd.read_csv('../../support/titanic_data.csv')  # create a DataFrame from a CSV

# df.head(number_of_rows) lets to get the first given number of rows
print(
    df_titanic.head(10)
)

# df.tail(number_of_rows) does the opposite than head()
print(
    df_titanic.tail(8)
)

# dataframe.dtypes shows the data type of each column
print('df_people column types:')
print(
    df_people.dtypes  # String are considered an Object
)


# df.describe()
print('df_animals.describe():')
print(
    df_animals.describe()  # it provides a quick overview just of the numerical data
)

# df.info()
# Shows more info about a df: current object type, rows, column names & types, if there is any null value, the df space
print('df_titanic info:')
print(
    df_titanic.info()
)


# df.shape
# It returns the number of rows and columns
print(f'df_titanic.shape: \n{df_titanic.shape}')


# notna() function - return not null values, it can be applied to columns or DataFrames
not_null_ages = df_titanic[df_titanic['Age'].notna()]

print('Not null Age values:')
print(
    not_null_ages
)
