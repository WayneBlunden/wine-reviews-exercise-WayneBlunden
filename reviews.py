# Bear with me this code is ugly. I'm sure there was an elegant solution through pandas but I couldn't find it.

# Import needed libraries
import pandas as pd
import zipfile
import os

# create dataframe with name df from file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip',compression='zip')
# Remove Unnamed column and setting index to country column
df = df.filter(['country', 'points'])

# Create a variable and pass all the unique values from the column country into it
CountryList = df.country.unique()

# Create dictionary to enter country, count, and mean into
CountDict = {}
# Iterate through each country in the variable CountryList, which is the list of unique countries from the dataframes 'country' column
for name in CountryList:
    # Create a temporary dataframe that contains only the points values for the current iteration 
    dfTemp = df.loc[df.country.isin([name])]
    # Count the total number of rows in the points column for the current iteration and assign it to variable 'count'
    Count = dfTemp.points.count()
    # Get the sum of the column labeled 'points' from the iterated dataframe
    Total = dfTemp['points'].sum()
    # Get the mean of the points scored for all rows from the current iteration
    Mean = Total / Count
    # Assign the current count and mean as a value assigned to the key named for the current iteration
    CountDict[name] = name, Count, Mean

# Create new dataframe using the dictionary created in for loop
dfFinal = pd.DataFrame(CountDict)
# Transpose the column to rows and using reset_index to prevent column headers from becoming an untouchable row element
dfFinal = dfFinal.T.reset_index()
# Removing row element created from old header names
dfFinal = dfFinal.drop('index', axis=1)
# Renaming column names
dfFinal.columns = ['country', 'count', 'points']
# Setting country column as the index for the rows
dfFinal.set_index('country', inplace=True)
# Sorting rows based off of count column value in descending order
dfFinal.sort_values('count', inplace=True, ascending=False)
# formatting float data types to one decimal point so points column shows as directed
pd.options.display.float_format = '{:,.1f}'.format

dir_path = os.path.dirname(os.path.realpath('reviews.ipynb'))
dfFinal.to_csv(dir_path + '/data/reviews-per-country.csv')