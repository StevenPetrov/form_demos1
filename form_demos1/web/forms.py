from django import forms
from django.db.models import TextField

OCCUPANCIES = (
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
)


class NameForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
        )
    age = forms.IntegerField(label='Your age')
    story = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us a story',
        }),
    )
    email = forms.CharField(widget=forms.EmailInput(), )
    password = forms.CharField(widget=forms.PasswordInput(), )
    occupancy = forms.ChoiceField(choices=OCCUPANCIES, )
    occupancy2 = forms.ChoiceField(choices=OCCUPANCIES, widget=forms.RadioSelect(), )
    occupancy3 = forms.ChoiceField(choices=OCCUPANCIES, widget=forms.SelectMultiple(), )
