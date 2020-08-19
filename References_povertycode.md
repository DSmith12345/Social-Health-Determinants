Census data package provides an array of functions to help access Census Bureau data.
General information about the package can be found where: https://pypi.org/project/CensusData/
For more detailed documentation please refer to: https://jtleider.github.io/censusdata/ 

Pandas is a package that allows for data shaping and analysis.
For more information about Pandas visit: https://pandas.pydata.org/

Technical documentation for ACS-1 and ACS-5:
https://www.census.gov/programs-surveys/acs/technical-documentation/summary-file-documentation.html
Appendices for each include table number, table topic, geography restrictions, summary file sequence number,
summary file starting and ending positions, topics, and universe. 

The countypov function takes in a integer StateNum which is used to call the poverty data for the 
corresponding state's counties. After this the function returns a data frame with the county poverty data.

The tractpov function takes in a integer StateNum which is used to call the poverty data for the 
corresponding state's census tracts. After this the function returns a data frame with the tract poverty data.
Note state numbers do not match with the Census Bureau state numbers, to find the numbers use:
censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2018) 