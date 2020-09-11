# Imports.
import pandas as pd
import censusdata
# Pandas options.
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# StateNum is the number of the state.
# Level is the granularity, e.g. county or tract.
# Code this the item that will be pulled from the Census Bureau.
# CodeName is the name that will appear on the column.
def cbdata (StateNum, Level, Code, CodeName):
        num = str(StateNum)
        level = Level
        code = Code
        name = CodeName
        
        if (level == "county" or level == "County"):
            data=censusdata.download('acs5', 2018, censusdata.censusgeo([('state', num),('county', '*')]),
                                    ['DP05_0001E', code],
                                    tabletype='profile')
            data['population']=data['DP05_0001E']
            data[name]=data[code]
            # Add two column to the table.
            data = data[['population',name]]
            
            # Parsing
            t = data
            t.reset_index(inplace=True)
            t.rename(columns={'index': 'longform'}, inplace=True)
            index = t.index
            # Parsing each counties information into a list of three strings: County, State, State and County Code.
            nrows = len(index)
            temp = []
            for i in index:
                a = t.iloc[i]['longform']
                b = str(a).split(',')
                temp.append(b)
            # Convert list into dataframe
            df = pd.DataFrame(temp, columns=['County','State','Level Code'])
            # Combine dataframes.
            result = pd.concat([df, t], axis=1, sort=False)
            final = result.drop(columns=['longform'])
            # Sort by value ascending.
            #data.sort_values(name, ascending=False, inplace=True)
            
        elif (level == "tract" or level == "Tract"):
            data=censusdata.download('acs5', 2018,
            censusdata.censusgeo([('state', num),('county', '*'),('tract','*')]),
            ['B00001_001E',code])
            
            data['population']=data['B00001_001E']
            #data[name]=round((data[code] / data['B00001_001E'])*100,2)
            data[name]=data[code]
            # Add two column to the table.
            data = data[['population',name]]
            
            # Parsing
            t = data
            t.reset_index(inplace=True)
            t.rename(columns={'index': 'longform'}, inplace=True)
            index = t.index
            # Parsing each counties information into a list of three strings: County, State, State and County Code.
            nrows = len(index)
            temp = []
            for i in index:
                a = t.iloc[i]['longform']
                b = str(a).split(',')
                temp.append(b)
            # Convert list into dataframe
            df = pd.DataFrame(temp, columns=['Track','County','State','Level Code'])
            # Combine dataframes.
            result = pd.concat([df, t], axis=1, sort=False)
            final = result.drop(columns=['longform'])
            # Sort by poverty percent.
            #data.sort_values(name, ascending=False, inplace=True)
            
        
        return final