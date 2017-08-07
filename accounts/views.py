from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import RegisterForm, CreateProfileForm

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

def create_profile(request):
	if request.method == 'POST':
		form = CreateProfileForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return redirect('accounts:view_profile')
	form = CreateProfileForm()
	return render(request, 'accounts/create_profile.html', {'form': form})

def view_profile(request, id=None):
	if id is not None:
		user = get_object_or_404(User, id=id)
	else:
		user = request.user
	return render(request, 'accounts/view_profile.html', {'user': user})
