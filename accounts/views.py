from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import (
	authenticate as django_auth,
	login as django_login
	)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login

from .models import Profile
from .forms import RegisterForm


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			# this thing creating profile using signals
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(useraname=user.username, password=raw_password)
			login(request, user)
			return redirect('home:home')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

def view_profile(request, id=None):
	if id is not None:
		user = get_object_or_404(User, id=id)
		user = user.profile
	else:
		user = request.user.profile
	return render(request, 'accounts/view_profile.html', {'user': user})

def change_profile(request, pk=None):
	return render(request, 'accounts/change_profile.html')

def login_view(request):
	print('cathced')
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
