# This text document is filled with tips and tricks that I encounted along the way. 

### See JSON structure 
Sees the structure of a JSON. 
```
data = r.json()
print(json.dumps(data, indent=2)) 
```
--- 
### Change data type in dataframe 
```
df['column_name'] = df['column_name'].astype("new_data_type") 
```
#### Example: 
```
df['properties_stationId'] = df['properties_stationId'].astype("int64") 
```