from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name', 'autofocus': ''}), max_length=40)

class FrameForm(forms.Form):
    attempt1 = forms.CharField(widget=forms.HiddenInput())
    attempt2 = forms.CharField(widget=forms.HiddenInput())
    attempt3 = forms.CharField(widget=forms.HiddenInput())
