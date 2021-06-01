from django import forms
from django import forms

class CandidateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    constituency = forms.CharField(label='Constituency', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    # change symbol to image later
    symbol = forms.CharField(label='Vote Symbol' , widget= forms.TextInput(attrs={'class':'form-field'}))
    