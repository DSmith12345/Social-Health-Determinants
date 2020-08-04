# Author Daniel Smith 
# Edited: 8/03/20
# Pulls poverty data from Census Bureau and exports to csv file.

# Imports.
import pandas as pd
import censusdata
# Pandas options.
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# Pulls data related to population and poverty.
# DP05_0001E is total population.
# DP03_0119PE is percent of poverty.
countyp=censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '51'),('county', '*')]),
                                   ['DP05_0001E','DP03_0119PE'],
                                   tabletype='profile')
countyp['population']=countyp['DP05_0001E']
countyp['percent_poverty']=countyp['DP03_0119PE']
# Add two column to the table.
countyp = countyp[['population','percent_poverty']]
# Sort by poverty percent.
countyp.sort_values('percent_poverty', ascending=False, inplace=True)
countyp.head(30)
# Sends to csv file name countypoverty.
censusdata.exportcsv('countypoverty.csv', countyp)

# Poverty data on tract level
tractpoverty = censusdata.download('acs5', 2018,
        censusdata.censusgeo([('state', '51'),('county', '*'),('tract','*')]),
        ['B00001_001E','B17010_001E','B17010_002E'])
# Population.
tractpoverty['population']= tractpoverty.B00001_001E
# Percent of poverty.
tractpoverty['percent_poverty'] = round((tractpoverty.B17010_002E/ tractpoverty.B17010_001E)*100,2)
# Adds columns to table.
tractpoverty = tractpoverty[['population', 'percent_poverty']]
# Sorts be percent of unemployment.
tractpoverty.sort_values('percent_poverty', ascending=True).head(30)
# Exports data to csv file name tractpoverty
censusdata.exportcsv('tractpoverty.csv', tractpoverty)