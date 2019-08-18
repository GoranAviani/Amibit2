from django.shortcuts import render
from amibit2.local_settings import locationiqTokenKey
# Create your views here.
from .making_requests import make_request_params

#returning users latitude and longitude
def get_user_lat_long(stringToSend):
    apiUrl = {"apiUrl": "https://eu1.locationiq.com/v1/"}
    apiEndpoint = {"apiEndpoint": "search.php"}
    params =  {"params1":{'key': locationiqTokenKey,
        'q': stringToSend,
        'format': 'json'}}
    result = make_request_params(**apiUrl, **apiEndpoint, **params)
    print(result)
    #get here lat and long
    return result