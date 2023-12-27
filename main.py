import requests
import json
import pandas as pd

# Connection
header = {"X-Gravitee-Api-Key": "99f4dd71-c763-4c07-a365-88f4ea95d47e"}
url = 'https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?'


params = {
    'stationId' : '06197',
    'limit' : '5',
    'parameterId' : 'humidity'
    # 'temp_dry'
}

# Request & Answer
r = requests.get(url=url, headers=header, params=params)

print(r.status_code)

# Converting the object r to json
data = r.json()

# Convert JSON to Pandas DataFrame
df = pd.json_normalize(data['features']) 

# TODO rename columns
df = df.rename(columns={'geometry.coordinates':'geometry_coordinates'})

df = df.sort_values(by=['properties.stationId', 'properties.observed'], ascending=False)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = df.loc[df['properties.stationId'] == '06197']

print(df)
