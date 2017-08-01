from django.shortcuts import render, redirect

from .models import UserProfile
from .forms import RegisterForm

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('accounts:make_profile')
	form = RegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

'''
def make_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.user = request.user
			form.save()
			return redirect('home:home')
	form = UserProfileForm()
	return render(request, 'accounts/make_profile.html', {'form': form})
'''