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

print(r.status_code)

# Converting the object r to json
data = r.json()

# Convert JSON to Pandas DataFrame
df = pd.json_normalize(data['features']) 

# TODO rename columns



# make this another file, where renaming is the main thing. 
col_names = {
    "geometry.coordinates" : 'geometry_coordinates',
    'geometry.type':'geometry_type',
    'properties.created':'properties_created',
    'properties.observed':'properties_observed',
    'properties.parameterId':'properties_parameterId',
    'properties.stationId':'properties_stationId',
    'properties.value':'properties_value'
    }

for col in col_names:
    df = df.rename(columns=col_names)


df = df.sort_values(by=['properties_observed'], ascending=False)

# WHAT THE FUCK MANNER
df['geometry_coordinates'] = df['geometry_coordinates'].astype("string")
df['properties_stationId'] = df['properties_stationId'].astype("int64")

print(df.dtypes)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

print(df)

# Assuming df is the DataFrame you want to upload
project_id = "my-project-399518"
table_id = 'my-project-399518.vejr_data.06074'

# Upload DataFrame to BigQuery with defined schema
pandas_gbq.to_gbq(df, table_id, project_id, if_exists="replace")