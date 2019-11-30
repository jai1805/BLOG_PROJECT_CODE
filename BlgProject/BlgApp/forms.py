from django.contrib.auth.models import User
from django import forms
from BlgApp.models import Upload
from django.urls import reverse



class SignupForms(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password','email','first_name','last_name')

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name','pic','description')
