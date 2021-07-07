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
    # symbol = forms.CharField(label='Vote Symbol' , widget= forms.TextInput(attrs={'class':'form-field'}))
    symbol = forms.FileField(
        label="Vote Symbol",
        widget=forms.FileInput(attrs={"class": "form-control mb-3"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})
