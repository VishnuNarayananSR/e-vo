from django import forms
class VoterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    voter_id = forms.IntegerField(label='Voter Id', widget= forms.TextInput(attrs={'class':'form-field'}))
    constituency = forms.CharField(label='Constituency', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    
class VoteForm(forms.Form):
    voter_id = forms.IntegerField(label='Voter Id', widget= forms.TextInput(attrs={'class':'form-field'}))
    vote_for = forms.CharField(label='Vote for', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    constituency = forms.CharField(label='Constituency', max_length=50, widget= forms.TextInput(attrs={'class':'form-field'}))
    symbol = forms.CharField(label='Vote Symbol' , widget= forms.TextInput(attrs={'class':'form-field'}))
