from django.shortcuts import render
from expandeduser.models import custom_user
from django.http import HttpResponse
from mobile_phone.models import user_phone

# Create your views here.

#This function witll return user mobile if user is approved and 
# wants to receive weather forecast
def get_user_mobile(user):
    try:
        user_phone_instance = user_phone.objects.get(userMobilePhone=user)
        #print(user_phone_instance)
        status = "OK"
        result = "9873505"
        return status, result        
    except:
        #user does not have anything in user phone model
        status = "DontSentSMS"
        result = ""
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

            status, result = get_user_mobile(user)
            print(status)
            print(result)

            if status == "DontSentSMS":
                pass # user mobile is not approved /does not want to receive sms
            else:
                pass



        else:
            pass



    return HttpResponse('Daily forecast sent to all users')