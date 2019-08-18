import requests
import json

def make_request_params(**kwargs):
    try:
        apiUrl = kwargs["apiUrl"]
    except:
        return ({"testing_apis function": "The main url for the API is missing"})

    try:
        apiEndpoint = kwargs["apiEndpoint"]
        # Add an endpoint to the api
        fullAPIUrl = apiUrl + apiEndpoint
    except:
        return ({"testing_apis": "The API endpoint for te API is missing"})

    try:
        params1 = kwargs["params1"]
        result = requests.get(fullAPIUrl, params=params1)
    except:
        return ({"testing_api": "Missing API data"})


    if result.status_code in (400, 401, 402, 403, 404):
        return result

    return result.json()

