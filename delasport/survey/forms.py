from django import forms
from models import RatingQuestion


class RatingForm(forms.Form):
    options = [('rating1', 'rating1'), ('rating2', 'rating2')]

    rating = forms.ChoiceField(choices=options, widget=forms.RadioSelect())

    class Meta:
        model = RatingQuestion
        fields = ['rating']