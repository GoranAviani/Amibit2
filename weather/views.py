from django.shortcuts import render
from expandeduser.models import custom_user
from django.http import HttpResponse
from mobile_phone.models import user_phone
from api_relay.views import get_user_lat_long, get_user_weather_forecast

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

#This function will send weather sms message to all users that have address and city
# and have been approved and want to receive sms messages
def send_daily_forecast_to_all(request):
    users = custom_user.objects.all()
    for user in users:
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
            print(userMobileStatus)
            print(userMobileNumber)

            if userMobileStatus == "DontSentSMS":
                pass # user mobile is not approved /does not want to receive sms
            else:
                #return users latitude and longitude from his address - api call
                #userLong = get_user_lat_long(stringToSend)
                userLat, userLong = get_user_lat_long(stringToSend)
                print(userLat)
                print(userLong)
                #return weather forecast for his lat and long
                weatherForecast = get_user_weather_forecast(userLat, userLong)
                print(weatherForecast)
                #send him a text message with weather forecast
                #all user checks have passed and he is to receive his forecast sms
                



        else:
            pass



    return HttpResponse('Daily forecast sent to all users')