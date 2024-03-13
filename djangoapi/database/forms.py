from django import forms
from . models import Member

class Memberforms(forms.ModelForm):
    class Meta:
        model=Member
        fields=['fname','lname','email','passwd','age']