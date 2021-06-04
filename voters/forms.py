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
