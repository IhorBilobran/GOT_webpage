from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import (
	authenticate as django_auth,
	login as django_login
	)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout

from .models import UserProfile
from .forms import RegisterForm, CreateProfileForm

'''
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],
									)
			login(request, new_user)
			return redirect('accounts:create_profile')

	form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})
'''

def register(request):

	return render(request, 'accounts/register.html')

def view_profile(request, id=None):
	if id is not None:
		user = get_object_or_404(User, id=id)
	else:
		user = request.user
	return render(request, 'accounts/view_profile.html', {'user': user})

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = django_auth(request, username=username, password=password)
		if user is not None:
			django_login(request, user)
			return redirect('home:home')
		return HttpResponse('Fuckin Error!!')
	return render(request, 'accounts/login.html')

@login_required
def logout_view(request, *args, **kwargs):
	logout(request, *args, **kwargs)
	return redirect('home:home')
