# Author Daniel Smith 
# Edited: 3/31/20
# Pulls poverty data from Census Bureau and exports to database.

# Imports.
import pandas as pd
import os
from CB_Data import cbdata
from DB_Upload import upload

server = os.environ.get('sdoh_con')

# Variables to be pulled for counties.
var_county =  {'population':'DP05_0001E', 'poverty_percent':'DP03_0119PE'}
# Variables to be pulled for tracts.
var_tract =  {'population':'B01001_001E', 'poverty_count':'B17001_002E'}
# Year of data.
Year = 2018

# Virginia data call.
VACounty = cbdata(51, Year,'county', var_county)
# West Virginia data call.
WVCounty = cbdata(54, Year,'county', var_county)
# Combines to one dataframe.
countypoverty = pd.concat([VACounty, WVCounty])
countypoverty = countypoverty.reset_index(drop=True)
# Adds extra columns
# Year
countypoverty['Year'] = ''
countypoverty['Year'][0] = Year
# Source
countypoverty['Source'] = ''
countypoverty['Source'][0] = 'CB ACS 5 Year'
# Variables
countypoverty['Variables'] = ''
var = list(var_county.keys())
for i in range(len(var)):
    countypoverty['Variables'][i]=var[i]

# Sends to data to database.
upload('poverty_county_test', countypoverty, server)

# Virginia data call.
VATract = cbdata(51, Year, 'tract',  var_tract)
# West Virginia data call.
WVTract = cbdata(54, Year, 'tract', var_tract)
# Combines to one dataframe.
tractpoverty = pd.concat([VATract, WVTract])
tractpoverty = tractpoverty.reset_index(drop=True)

# Exports data to database.
upload('poverty_tract_test', tractpoverty, server)
