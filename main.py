import requests
import json
import pandas as pd
import pandas_gbq
from google.cloud import bigquery

# Connection
header = {"X-Gravitee-Api-Key": "99f4dd71-c763-4c07-a365-88f4ea95d47e"}
url = 'https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?'

params = {
    'stationId' : '06074',
    'limit' : '10',
    'parameterId' : 'temp_dry'
}

# Request & Answer
r = requests.get(url=url, headers=header, params=params)

# Converting the object r to json
data = r.json()

# Convert JSON to Pandas DataFrame
df = pd.json_normalize(data['features']) 

# Removing unnecessary columns 
df = df.drop(columns=['type', 'properties.created', 'geometry.type'])

# Naming the columns so the to_gbq funciton doesn't fail because of incorrect naming.
col_names = {
    'id' : 'id',
    'geometry.coordinates' : 'geometry_coordinates',
    'properties.observed':'properties_observed',
    'properties.parameterId':'properties_parameterId',
    'properties.stationId':'properties_stationId',
    'properties.value':'properties_value'
    }
for col in col_names:
    df = df.rename(columns=col_names)

# Explicitly set the data types
# setting columns that are supposed to be strings
string_columns = [
    'id', 
    'geometry_coordinates', 
    'properties_observed', 
    'properties_parameterId', 
    'properties_stationId'
] 
df[string_columns] = df[string_columns].astype('string')

# setting columns that are supposed to be float
float_columns = [
    'properties_value'
]
df[float_columns] = df[float_columns].astype(float)

# Sorting so the newest observations comes first
df = df.sort_values(by=['properties_observed'], ascending=False)

# Printing types (only for local testing)
print(df.dtypes)
print(df)

# Assuming df is the DataFrame you want to upload
project_id = "my-project-399518"
table_id = 'my-project-399518.vejr_data.06074'

# Upload DataFrame to BigQuery with defined schema
pandas_gbq.to_gbq(df, table_id, project_id, if_exists="replace")