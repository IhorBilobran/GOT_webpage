from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile

class RegisterForm(UserCreationForm):
	city = forms.CharField(max_length=50)
	class Meta:
		model = User
		fields = (
				"username", "email", 'first_name', 'city',
				'last_name', "password1", "password2",
				'email'	)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
			'placeholder': 'First name',
		})
		self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
			'placeholder': 'Lirst name',
		})
		self.fields['email'].widget.attrs.update({
	         'class': 'form-control',
			 'placeholder': 'your@mail.com',
		})
		self.fields['username'].widget.attrs.update({
	         'class': 'form-control',
			 'placeholder': 'Username',
		})
		self.fields['password1'].widget.attrs.update({
	         'class': 'form-control',
			 'placeholder': 'Password',
		})
		self.fields['password2'].widget.attrs.update({
	         'class': 'form-control',
			 'placeholder': 'Confirm your password',
		})

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class ProfileUpdateForm(UserChangeForm):

	class Meta:
		model = Profile
		fields = (
			'house', 'img', 'city', 'password'
		)

	def __init__(self, *args, **kwargs):
		super(ProfileUpdateForm, self).__init__(*args, **kwargs)
#		self.fields['first_name'].widget.attrs.update({
#			'class': 'form-control',
#			'placeholder': 'first_name'
#	})
