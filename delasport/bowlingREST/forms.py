from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name', 'autofocus': ''}), max_length=40)
