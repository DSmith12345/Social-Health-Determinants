# Author Daniel Smith 
# Edited: 9/28/20
# Pulls poverty data from Census Bureau and exports to database.

# Imports.
import pandas as pd
import censusdata
import configparser
import urllib
from sqlalchemy import create_engine
from CB_Data import cbdata
from DB_Upload import upload
# Pandas options.
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# Pulls data related to population and poverty.
# DP05_0001E is total population.
# DP03_0119PE is percent of poverty.

#
with open('server.txt', 'r') as file:
    server = file.read()

# Variables to be pulled for counties.
var_county =  {'population':'DP05_0001E', 'poverty_percent':'DP03_0119PE'}
# Variables to be pulled for tracts.
var_tract =  {'population':'B01001_001E', 'poverty_count':'B17001_002E'}

# Virginia data call.
VACounty = cbdata(51, 'county', var_county)
# West Virginia data call.
WVCounty = cbdata(54, 'county', var_county)
# Combines to one dataframe.
countypoverty = pd.concat([VACounty, WVCounty])

# Sends to data to database.
upload('poverty_county', countypoverty, server)

# Virginia data call.
VATract = cbdata(51, 'tract',  var_tract)
# West Virginia data call.
WVTract = cbdata(54, 'tract', var_tract)
# Combines to one dataframe.
tractpoverty = pd.concat([VATract, WVTract])

# Exports data to database.
upload('poverty_tract', tractpoverty, server)
