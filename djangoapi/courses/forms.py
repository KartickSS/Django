from django import forms
from . models import Company_income

class Income_table(forms.ModelForm):
    class Meta:
        model=Company_income
        fields=['Date','Grocery','Bakery','Clothes','Electronics']