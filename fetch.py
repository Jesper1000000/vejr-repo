import requests

def fetchData(stationId="06074", limit="10", parameterId=["temp_dry"]) -> dict: 
    '''
    Description:
    Connects to the API, transforms the response object to a Python dict, and returns it as data.

    Args: 
    station_id (str): The station ID for the observation.
    limit (str): The limit for the number of observations.
    parameter_id (str): The parameter for the observation.

    Return: 
    Returns data as a dictionary (dict). 
    '''
    
    # Connection
    header = {"X-Gravitee-Api-Key": "99f4dd71-c763-4c07-a365-88f4ea95d47e"}
    url = 'https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?'

    # settings
    params = {
    'stationId' : stationId,
    'limit' : limit,
    'parameterId' : parameterId
    }

    print(url)
    # Request & Answer
    r = requests.get(url=url, headers=header, params=params)
    
    # Converting the object r to python dict    
    data = r.json()

    return data