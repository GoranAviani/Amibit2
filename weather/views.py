from django.shortcuts import render
from expandeduser.models import custom_user
from django.http import HttpResponse
from mobile_phone.models import user_phone
from api_relay.views import get_user_lat_long_api, get_user_weather_forecast_api, send_sms_message_api
import time

# Create your views here.

def get_mobile_phone(user_phone_instance):
    if (user_phone_instance.isMobileValidated == True and user_phone_instance.sendWeatherSMS == True):
        #print(user_phone_instance)
        if (user_phone_instance.phoneCountryCode != None and user_phone_instance.phoneCountryCode != None):
            phoneCountryCode = user_phone_instance.phoneCountryCode
            phoneNumber = user_phone_instance.phoneNumber
        
            status = "OK"
            result = phoneCountryCode + phoneNumber
            return status, result
        else:
            status = "DontSentSMS"
            result = ""
            return status, result
    else:
        status = "DontSentSMS"
        result = ""
        return status, result

def process_forecast_for_sms_message(result, userCity):
    processedMessage = ("Hi, this is your daily forecast for {}! Now its {} degrees. Todays lowest temp: {}, highest: {}. The weather will be: {} Your Amibit!" 
    .format(userCity, str(result["currently"]["temperature"]),
    str(result["daily"]["data"][0]["temperatureLow"]),
    str(result["daily"]["data"][0]["temperatureHigh"]), 
    str(result["hourly"]["summary"]) ) )

    #print(result["currently"]["summary"]) # this
    #print(result["currently"]["temperature"]) #this
    #print(result["currently"]["uvIndex"])

    #print(result["hourly"])
    #print(result["hourly"]["summary"]) #need this


    return processedMessage

#This function witll return user mobile if user is approved and 
# wants to receive weather forecast
def get_user_mobile_status(user):
    try:
        user_phone_instance = user_phone.objects.get(userMobilePhone=user)     
    except:
        #user does not have anything in user phone model
        status = "DontSentSMS"
        result = ""
        return status, result

    status, result = get_mobile_phone(user_phone_instance)
    return status, result

#the actual sending of the forecast
def send_daily_forecast(user):
    stringToSend =""
    userAddress = user.userAddress
    userCity = user.userCity
    userCountry = user.userCountry

    if (userCountry != None and userCountry != None):
        if userAddress != None:
            stringToSend = str(userAddress) + "," + str(userCity)+ "," + str(userCountry)
        else:
            stringToSend = str(userCity) + "," + str(userCountry)

        userMobileStatus, userMobileNumber = get_user_mobile_status(user)
        #print(userMobileStatus)
        #print(userMobileNumber)

        if userMobileStatus == "DontSentSMS":
            pass # user mobile is not approved /does not want to receive sms
        else:
            #all user checks have passed and he is to receive his forecast sms
            
            #return users latitude and longitude from his address - api call
            #userLong = get_user_lat_long(stringToSend)
            userLat, userLong = get_user_lat_long_api(stringToSend)
            #print(userLat)
            #print(userLong)
                
            #return weather forecast for his lat and long
            weatherForecast = get_user_weather_forecast_api(userLat, userLong)
            processedForecastMessage = process_forecast_for_sms_message(weatherForecast, userCity)
            #print(processedForecastMessage)
            
            #delay of 0.5s because free Twilio account supports 2 messages in a second.
            #if number is greather than that twilio will return 429 code.
            time.sleep(0.5)
            #send him a text message with weather forecast
            send_sms_message_api(userMobileNumber, processedForecastMessage)

    else:
        pass


    




#This function will send weather sms message to all users that have address and city
# and have been approved and want to receive sms messages
def send_daily_forecast_to_all(request):
    users = custom_user.objects.all()
    for user in users:
        send_daily_forecast(user)
    return HttpResponse('Daily forecast sent to all users')



def send_daily_forecast_to_user(request):
    user = request.user
    send_daily_forecast(user)
    return HttpResponse('Daily forecast has been sent to {}' .format(user.username))
