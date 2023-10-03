from django import forms
from accounts.models import user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class user_form(UserCreationForm):
    class Meta : 
        model = User
        fields = ['username','email','password1','password2']
    captcha = ReCaptchaField()

class user_profile_form(forms.ModelForm):
    class Meta :
        model = user_model
        fields = ['user_img']