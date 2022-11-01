import pandas as pd

# ------------------------------------------------------------------------------------------------------
# where function
# ------------------------------------------------------------------------------------------------------

# It replaces rows data which meets certain condition
# All the data that does not meet the condition is replaced by NaN value by default
# It replaces all the columns values for the given value or NaN in each row that meets the condition

nba_players = pd.read_csv('../../support/nba.csv')

# inplace attribute allows to modify the original DataFrame instead of returning a new one
nba_players.sort_values('Team', inplace=True)


atlanta_hawks_filter = nba_players['Team'] == 'Atlanta Hawks'

# where() structure:
# df.where(series_or_conditions, substitution_value, inplace=)
atlanta_hawks_players_info = nba_players.where(atlanta_hawks_filter)


print('Original NBA players table:')
print(nba_players)

print('New NBA players table only with Atlanta Hawks players info:')
print(atlanta_hawks_players_info)  # Non Atalanta players are marked with NaN


df_titanic = pd.read_csv('../../support/titanic_data.csv')

df_titanic.sort_values('Name', inplace=True)

male_passengers_filter = df_titanic['Sex'] == 'male'
above_35_years = df_titanic['Age'] >= 35

# Applying to filters in where function
male_result = df_titanic.where(male_passengers_filter & above_35_years, 'NA')
# NA value is applied in every row cell that does not meet the conditions

print('male passengers:')
print(male_result[['Name', 'Sex']])
