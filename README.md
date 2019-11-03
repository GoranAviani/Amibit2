# Amibit 2

An online perosnal bookmark and notes manager. Amibit is built as a replacement for Firefox or Chrome most visited page and new tab page.

Beside ofering the usual username/password user authentication Amibit also offers Google's user authentication of using OAuth 2 protocols. 

After registration users are redirected to their personal dashboards where they manage their notes and links.


https://amibit.org



# Prerequisites
certifi==2019.3.9
chardet==3.0.4
defusedxml==0.5.0
Django==2.2.4
idna==2.8
oauthlib==3.0.1
psycopg2==2.7.7
psycopg2-binary==2.7.7
PyJWT==1.7.1
PySocks==1.7.0
python3-openid==3.1.0
pytz==2018.9
requests==2.21.0
requests-oauthlib==1.2.0
six==1.12.0
social-auth-app-django==3.1.0
social-auth-core==3.1.0
sqlparse==0.3.0
twilio==6.29.3
urllib3==1.24.1


# Installing

Make sure to create your virtualenv before installing requirements. Create your own virtualenv, preferably using virtualenvwrapper and install dependancies inside.

mkvirtualenv your_env_name

pip install -r requirements.txt

To start using the Django app you first need to set up postgresql and make django migrations.



# Notes/ Additional Info
# Authors

    * Goran Aviani - Software Engineer
