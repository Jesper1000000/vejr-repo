# This text document is filled with tips and tricks that I encounted along the way. 

### See JSON structure 
Sees the structure of a JSON. 
```
data = r.json()
print(json.dumps(data, indent=2)) 
```
--- 

### Change data type in dataframe 

Thanks to this article: https://saturncloud.io/blog/python-pandas-converting-object-to-string-type-in-dataframes/

```
list_name = [
    'column_name', 
    'column_name', 
    'column_name', 
    'column_name', 
    'column_name'
]
df[list_name] = df[list_name].astype('string')
```
#### Example shows converting columns to string: 
```
string_columns = [
    'id', 
    'geometry_coordinates', 
    'properties_observed', 
    'properties_parameterId', 
    'properties_stationId'
]
df[string_columns] = df[string_columns].astype('string')
```
---

### Show all pandas cols no matter what (I think)

The code: 
```
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
```

#### Filter Pandas DataFrames by Column of multiple Strings

Thanks to this article: https://saturncloud.io/blog/how-to-filter-pandas-dataframes-by-column-of-strings/

```
df = df[df["column_name"].str.contains("parameter|another_parameter")]
```

#### Example 
```
df = df[df["properties.parameterId"].str.contains("temp_dry|temp_dew")]
```