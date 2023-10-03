from django import forms 
from bankaccounts.models import KYC
from django.forms import DateInput,FileInput

class Dateinput(forms.DateInput):
    input_type = 'date'

class KYC_form(forms.ModelForm):
    identity_image = forms.ImageField(widget=FileInput)
    image = forms.ImageField(widget=FileInput)
    signature = forms.ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = [
            'full_name',
            'image',
            'gender',
            'identity_type',
            'identity_image',
            'date_of_birth',
            'signature',
            'country',
            'state',
            'city',
            'phone',
            'email'
        ]
    widget = {
        'date_of_birth' : DateInput
    }