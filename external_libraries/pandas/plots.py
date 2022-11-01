import pandas as pd

import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------------------
# plot
# ------------------------------------------------------------------------------------------------------
# It creates data graphs of DataFrame or Series

# index_col= define a column to be used as the index
# parse_dates= converts dates into a Timestamp object
air_quality = pd.read_csv('../../support/air_quality_no2.csv', index_col=0, parse_dates=True)

print(
    air_quality.head()
)


# Creating a linear graph of every column, plot
air_quality.plot()

# It renders the created plot
plt.show()


# Plotting just a single column
# df['column_name'].plot()
air_quality['station_paris'].plot()

plt.show()


# plot.scatter()
# It visually compares values among columns

# define x and y graph coordinates with their columns
air_quality.plot.scatter(x='station_london', y='station_paris', alpha=0.5)

plt.show()


# plot.box()
# It generates a boxplot graph
air_quality.plot.box()
plt.show()


# plot.area
# Separate each column in its own plot
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)  # subplots option to allow other plots creation
plt.show()


# Custom plots
fig, axs = plt.subplots(figsize=(12, 4))                # Create an empty Matplotlib Figure and Axes
air_quality.plot.area(ax=axs)                           # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")                  # Do any Matplotlib customization you like
fig.savefig("../../support/no2_concentrations.png")     # Save the Figure/Axes using the existing Matplotlib method.
plt.show()                                              # Display the plot

