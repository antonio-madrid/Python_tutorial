from external_libraries.pandas.common.common_dataframes import df, df_animals

# ------------------------------------------------------------------------------------------------------
# Series
# ------------------------------------------------------------------------------------------------------
# Series is a two dimensions array which symbolizes all the column values and its row index
print('\nSeries:\n')

# Get all the values allocated in a Column
# dataframe_name['Column_Name'] = Dictionary['Key']
print(
    df['Column1']  # returns a Series
)

# Series common operations

# Series has not column names, because it is a single column
print("Series of df['Column1'] max value:")
print(
    df['Column1'].max()
)

# Series.dtypes shows the data type of the represented column
num_legs_column = df_animals['num_legs']
print('df_animals num_legs column type:')
print(
    num_legs_column.dtypes
)
