from django import forms
#from .models import custom_user
from .models import link

class create_link_form(forms.ModelForm):
    link_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    link_url = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    class Meta:
        model = link
        fields = (
            'link_name',
            'link_url',
)