from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import custom_user

#class UserCreationForm A ModelForm for creating a new user.
#It has three fields: username (from the user model), password1, and password2. It verifies that password1 and password2 match, validates the password using validate_password(), and sets the user’s password using set_password().
class custom_user_creation_form(UserCreationForm):

    class Meta(UserCreationForm):
        model = custom_user
        fields = ('username', 'email')


#class UserChangeForm A form used in the admin interface to change a user’s information and permissions.
class custom_user_change_form(UserChangeForm):

   class Meta:
        model = custom_user
        fields = ('username', 'email')


class user_profile_form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class':'nekicss'}))

    class Meta:
        model = custom_user
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'userSecondEmail',
            'userDoB',
            'userCountry',
            'userCity',
            'userMobilenumber',
)
        