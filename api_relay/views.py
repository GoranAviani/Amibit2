from django.shortcuts import render
from amibit2.local_settings import locationiqTokenKey, darkSkyToken

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
    #get here lat and long
    userLat = result[0]["lat"]
    userLon = result[0]["lon"]

    return userLat, userLon


def get_user_weather_forecast(userLen, userLong):
    
    apiUrl = {"apiUrl": "https://api.darksky.net/forecast/"}
    apiEndpoint = {"apiEndpoint": darkSkyToken + "/" + userLen +","+userLong}
    params =  {"params1":{'units': "auto",}}
    result = make_request_params(**apiUrl, **apiEndpoint, **params)
    print(result)
    return result