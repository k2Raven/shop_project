from django import forms


class SimpleSearchForm(forms.Form):
    search = forms.CharField(label='Найти', required=False)