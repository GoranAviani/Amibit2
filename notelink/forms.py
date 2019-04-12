from django import forms
#from .models import custom_user
from .models import link

class create_link_form(forms.ModelForm):
    linkName = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    linkUrl = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    class Meta:
        model = link
        fields = (
            'linkName',
            'linkUrl',
)