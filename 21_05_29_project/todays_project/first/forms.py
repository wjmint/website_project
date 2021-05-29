from django import forms

class User(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email   = forms.EmailField()