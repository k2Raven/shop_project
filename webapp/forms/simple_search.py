from django import forms
from django.utils.translation import gettext_lazy as _


class SimpleSearchForm(forms.Form):
    search = forms.CharField(label=_('Найти'), required=False)