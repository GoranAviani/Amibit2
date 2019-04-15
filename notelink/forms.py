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
    noteTitle = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    noteText = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'note-text-input'}))
    class Meta:
        model = note
        fields = (
            'noteTitle',
            'noteText',
)

class update_note_form(forms.ModelForm):
    noteTitle = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    noteText = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'note-text-input'}))
    noteTimestamp = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'note-text-input'}))
    
    class Meta:
        model = note
        fields = (
            'noteTitle',
            'noteText',
            'noteTimestamp',
)