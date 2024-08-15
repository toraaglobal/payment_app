from django import forms
from account.models import  KYC
from userauths.models import User
from django.forms import ImageField, FileField,DateInput


class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=forms.FileInput)
    image = ImageField(widget=forms.FileInput)
    signature = ImageField(widget=forms.FileInput)

    class Meta:
        model = KYC
        fields = ['full_name', 'identity_type', 'identity_number', 'identity_image',
                   'marital_status','signature','date_of_birth','country','state','city','mobile','fax','image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}),
            'fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fax'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'state':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'city':forms.TextInput(attrs={'placeholder': 'City'}),
            "date_of_birth": DateInput(),
        }