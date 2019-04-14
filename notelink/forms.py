from django import forms
#from .models import custom_user
from .models import link, note

class create_link_form(forms.ModelForm):
    linkName = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    linkUrl = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    class Meta:
        model = link
        fields = (
            'linkName',
            'linkUrl',
)



class create_note_form(forms.ModelForm):
    note_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    note_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'note-text-input'}))
    class Meta:
        model = note
        fields = (
            'note_title',
            'note_text',
)