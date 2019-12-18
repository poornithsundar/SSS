from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Narayana_Submission
from django import forms
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
	username=forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'place-holder':'Username'
		}))
	password=forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'place-holder':'Password'
		}))

class SaveForm(forms.Form):
	user = forms.CharField(label="Username")
	data = JSONField()
	score = forms.IntegerField()