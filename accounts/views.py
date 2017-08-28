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
from .forms import RegisterForm, ProfileUpdateForm
from home.models import House

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			# this thing creating profile using signals
			user.profile.city = form.cleaned_data.get('city')
			user.save()
			return redirect('home:home')
	else:
		form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

def view_profile(request, id=None):
	if id is not None:
		user = get_object_or_404(User, id=id)
		args = {'user': user}
	else:
		user = request.user
		args = {'user': user}
	users = User.objects.all()
	args['users'] = users
	return render(request, 'accounts/view_profile.html', args)

def change_profile(request, pk=None):
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user.profile.house = form.cleaned_data.get('house')
			user.profile.img = form.cleaned_data.get('img')
			user.profile.city = form.cleaned_data.get('city')
			user.save()
			return redirect('accounts:view_profile')
		print(form.errors)
		return HttpResponse('fuckin error')
	form = ProfileUpdateForm(instance=request.user)
	house_choice = [x for x in House.objects.all()]
	form.user = request.user
	profile = request.user.profile
	args = {'form': form, 'profile': profile, 'house_choice': house_choice}
	return render(request, 'accounts/change_profile.html', args)

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
