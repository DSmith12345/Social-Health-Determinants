# Function for pulling multiple years for acs variables.
from CB_Data import cbdata
import pandas as pd

# yearlist is the years of the acs to be pulled.
# StateNum is the number of the state be pulled.
# Level of acs data.
# variables are the measures to be pulled from the acs.
def years(yearlist, StateNum, level, variables):
    # Pulls all data from select years.
    data = []
    N = len(yearlist)
    for i in range(N):
        data.append(cbdata(StateNum,yearlist[i],level,variables))
    
    # Combine years of measures into one dataframe.
    df = data[0].sort_values('County')
    df = df.reset_index(drop=True)
    for i in range(N-1):
        # 
        temp = data[i+1]
        s = temp.sort_values('County')
        s = s.reset_index(drop=True)
        df = pd.concat([df, s.iloc[:, 4:4+N]], axis=1)
        
    final = df.reset_index(drop=True)
    return final