from django import forms


class CandidateForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    constituency = forms.CharField(
        label="Constituency",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    # change symbol to image later
    # symbol = forms.CharField(label='Vote Symbol' , widget= forms.TextInput(attrs={'class':'form-field'}))
    symbol = forms.FileField(
        label="Vote Symbol",
        widget=forms.FileInput(attrs={"class": "form-control mb-3"}),
    )
