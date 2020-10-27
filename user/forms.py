from django import forms
from . models import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [  'firstName', 'lastName', 'ssn', 'age' ]

    def clean_ssn(self):
        ssn = self.cleaned_data.get('ssn')
        if len(ssn) != 9:
            raise forms.ValidationError("Error, ssn must be 9 digits.")
        return ssn[0]+ssn[1]+ssn[2]+'-'+ssn[3]+ssn[4]+'-'+ssn[5]+ssn[6]+ssn[7]

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 130 or age < 18:
            raise forms.ValidationError("Error, invalid age (18-130).")
        return age