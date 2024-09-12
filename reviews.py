# import csv and pandas library and set alias of pd for pandas 
import pandas as pd
import csv
# importing zipfile library
import zipfile
# creating dataframe from provided csv.zip file. 
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip',compression='zip')

df = dr.drop()


## setting the index for the dataframe to the column labeled country
## df.set_index('country', inplace=True)
## create a second dataframe that will be manipulated
# Create a variable and pass the unique list of countries from df into it
UniqueCountry = df['country'].unique().tolist()
ReviewCount = df['country'].value_counts()
#AverageScore = 
 
dfWork = pd.DataFrame()
dfWork.columns = ['country', 'count', 'points']





#dfWork = pd.DataFrame(ReviewCount, AverageScore)
#data = df.columns

print(dfWork)

