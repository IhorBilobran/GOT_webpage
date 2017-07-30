from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import House, Person

class Home(View):
	template_name = 'home/home.html'

	def get(self, request):
		houses = House.objects.all()
		persons = Person.objects.all()
		args = {'houses': houses, 'persons': persons}

		return render(request, self.template_name, args)

	def post(self, request):
		pass

def view_house(request, id=None):
	if id is not None:
		house = get_object_or_404(House, id=id)
		persons = Person.objects.filter(house__id=id)
		args = {'house': house, 'persons': persons}
	else:
		return redirect('home:home')
	return render(request, 'home/view_house.html', args)