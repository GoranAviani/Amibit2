from django import forms
from .models import user_phone

class user_mobile_phone_form(forms.ModelForm):
    phoneCountryCode = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control'}))
    phoneNumber = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = user_phone
        fields = (
            'phoneCountryCode',
            'phoneNumber',
)