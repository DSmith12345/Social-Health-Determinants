# Author Daniel Smith 
# Edited: 8/11/20
# Pulls poverty data from Census Bureau and exports to csv file.

# Imports.
import pandas as pd
import censusdata
#TODO import cbdata and dpbupload from current directory
# Pandas options.
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# Pulls data related to population and poverty.
# DP05_0001E is total population.
# DP03_0119PE is percent of poverty.

#TODO: replace countypov with cb_data
def countypov (StateNum):
        num = str(StateNum)
        
        countyp=censusdata.download('acs5', 2018, censusdata.censusgeo([('state', num),('county', '*')]),
                                   ['DP05_0001E','DP03_0119PE'],
                                   tabletype='profile')
        countyp['population']=countyp['DP05_0001E']
        countyp['percent_poverty']=countyp['DP03_0119PE']
        # Add two column to the table.
        countyp = countyp[['population','percent_poverty']]
        # Sort by poverty percent.
        countyp.sort_values('percent_poverty', ascending=False, inplace=True)
        countyp.head(30)
        
        return countyp

# Virginia data call.
VACounty = countypov(51)
# West Virginia data call.
WVCounty = countypov(54)
# Combines to one dataframe.
countypoverty = pd.concat([VACounty, WVCounty])

# Sends to csv file name countypoverty.
#TODO: Add DB_Upload call here to replace csv export
upload('poverty_county', con = engine)
censusdata.exportcsv('countypoverty.csv', countypoverty)

#TODO: replace tractpov with cb_data
def tractpov(StateNum):
        num = str(StateNum)
        tractp = censusdata.download('acs5', 2018,
        censusdata.censusgeo([('state', num),('county', '*'),('tract','*')]),
        ['B00001_001E','B17010_001E','B17010_002E'])
        # Population.
        tractp['population']= tractp.B00001_001E
        # Percent of poverty.
        tractp['percent_poverty'] = round((tractp.B17010_002E/ tractp.B17010_001E)*100,2)
        # Adds columns to table.
        tractp = tractp[['population', 'percent_poverty']]
        return tractp

# Virginia data call.
VATract = tractpov(51)
# West Virginia data call.
WVTract = tractpov(54)
# Combines to one dataframe.
tractpoverty = pd.concat([VATract, WVTract])

# Exports data to csv file name tractpoverty
#TODO: Add DB_Upload call here to replace csv export
upload('poverty_tract', con = engine)
censusdata.exportcsv('tractpoverty.csv', tractpoverty)

import urllib
from sqlalchemy import create_engine
params= urllib.parse.quote_plus("DSN=cca_qa")
engine = create_engine("netezza+pyodbc:///?odbc_connect=%s" % params,  echo=True)

