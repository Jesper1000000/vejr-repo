import pandas as pd
import pandas_gbq
from fetch import fetchData

data = fetchData(stationId='06074', limit=100, parameterId=[None])

df = pd.json_normalize(data['features']) 

df = df.drop(columns=['type', 'properties.created', 'geometry.type'])

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

df = df[df["properties_parameterId"].str.contains("temp_dry")]

string_columns = [
    'id', 
    'geometry_coordinates', 
    'properties_observed', 
    'properties_parameterId', 
    'properties_stationId'
]
df[string_columns] = df[string_columns].astype('string')
df[string_columns] = df[string_columns].fillna('Na')

float_columns = [
    'properties_value'
]
df[float_columns] = df[float_columns].astype(float)
df[float_columns] = df[float_columns].fillna(0.0)

df = df.sort_values(by=['properties_observed'], ascending=False)

print(df)

project_id = "my-project-399518"
table_id = 'my-project-399518.vejr_data.06074'

# pandas_gbq.to_gbq(df, table_id, project_id, if_exists="replace")