import psycopg2
import sqlalchemy
import pandas as pd
from CB_Data import cbdata

# TableName is the name of the table that will be created in the database.
# Dataframe is the pandas dataframe that will be upload to the database.
# DB is the location of the database. example: postgresql://postgres:Password@localhost/DatabaseName
def upload(TableName, Dataframe ,DB):
    
    name = str(TableName)
   
    db = str(DB)
    
    # Read in dataset (pandas format).
    df = Dataframe

    # Connects to data base.
    engine = sqlalchemy.create_engine(db)
    con = engine.connect()

    # Adds table to data base.
    df.to_sql(name, con)

    con.close()
    
    return 1
