# Imports.
import pandas as pd
import censusdata
# Pandas options.
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# StateNum is the number of the state.
# Year of the data to be pulled.
# Level is the granularity, e.g. county or tract.
# Variables is a dictionary that takes in the names and variables that will be pulled.
# Example: {'population':'DP05_0001E', 'poverty_percent':'DP03_0119PE'}
def cbdata (StateNum, Year, Level, Variables):
        num = str(StateNum)
        y = int(Year)
        level = Level
        dictionary = Variables
        codes = list(dictionary.values())
        names = list(dictionary.keys())
        
        if (level == "county" or level == "County"):
            data=censusdata.download('acs5', y, censusdata.censusgeo([('state', num),('county', '*')]), codes, tabletype='profile')
            
            niter = len(codes)
            for i in range(niter):
                data[names[i]]=data[codes[i]] 
            
            # Adds column names.
            data = data[names]
            
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
                
                a = t.iloc[i]['longform']
                b = str(a).split(',')
                # State cleaning.
                d = b[1]
                d = d.split(':' )[0]
                b[1]=d
                # Splits state number and county number.
                d = b[2]
                d1 = d.split('>')[0] 
                d2 = d.split('>')[1]
                d1 = d1.split(':')[1] # State number
                d2 = (d2.split(':')[1]) # County number
                b[2]=d2
                b.append(d1)
                #
                c = map(str.strip, b) # Removes whitespaces.
                temp.append(c)
            # Convert list into dataframe
            df = pd.DataFrame(temp, columns=['County','State','County_Number','State_Number'])
            # Combine dataframes.
            result = pd.concat([df, t], axis=1, sort=False)
            final = result.drop(columns=['longform'])
            
        elif (level == "tract" or level == "Tract"):
            data=censusdata.download('acs5', y,
            censusdata.censusgeo([('state', num),('county', '*'),('tract','*')]),codes)
            
            niter = len(codes)
            for i in range(niter):
                data[names[i]]=data[codes[i]]
            
            # Adds column names
            data = data[names]
            
            # Parsing
            t = data
            t.reset_index(inplace=True)
            t.rename(columns={'index': 'longform'}, inplace=True)
            index = t.index
            # Parsing each counties information into a list of three strings: Tract, County, State, State and County Code.
            nrows = len(index)
            temp = []
            for i in index:
                a = t.iloc[i]['longform']
                b = str(a).split(',')
                # Tract cleaning.
                d = b[0]
                d = d.split(' ')[2]
                b[0]=d
                # State cleaning.
                d = b[2]
                d = d.split(':' )[0]
                b[2]=d
                # Splits state number and county number.
                d = b[3]
                d1 = d.split('>')[0] 
                d2 = d.split('>')[1]
                d1 = d1.split(':')[1] # State number
                d2 = d2.split(':')[1] # County number
                b[3]=d2
                b.append(d1)
                #
                c = map(str.strip, b) # Removes whitespaces.
                temp.append(c)
            # Convert list into dataframe
            df = pd.DataFrame(temp, columns=['Tract','County','State','County_Number','State_Number'])
            # Combine dataframes.
            result = pd.concat([df, t], axis=1, sort=False)
            final = result.drop(columns=['longform'])
        
        return final