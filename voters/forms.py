from django import forms


class VoterForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    voter_id = forms.IntegerField(
        label="Voter Id", widget=forms.TextInput(attrs={"class": "form-control mb-3"})
    )
    constituency = forms.CharField(
        label="Constituency",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    voter_img = forms.FileField(
        label="Voter Image",
        widget=forms.FileInput(attrs={"class": "form-control mb-3"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})

class VoteForm(forms.Form):
    voter_id = forms.IntegerField(
        label="Voter Id", widget=forms.TextInput(attrs={"class": "form-control mb-3"})
    )
    constituency = forms.CharField(
        label="Constituency",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    vote_for = forms.CharField(
        label="",
        max_length=50,
        widget=forms.HiddenInput(
            attrs={"class": "form-control mb-3", "id": "candidate-input"}
        ),
    )
    symbol = forms.CharField(
        label="",
        widget=forms.HiddenInput(
            attrs={"class": "form-control mb-3", "id": "symbol-input"}
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})