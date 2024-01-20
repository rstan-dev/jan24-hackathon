from django import forms

class MyForm(forms.Form):
    categories = forms.CharField()
