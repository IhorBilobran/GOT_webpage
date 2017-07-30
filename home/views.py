from django.shortcuts import render, get_object_or_404, redirect
#sfrom django.views import View

from .models import House, Person, Castel


def home(request):
	return render(request, 'index.html')

def house_gallery(request):
	houses = House.objects.all().order_by('name')
	persons = Person.objects.all()
	args = {'houses': houses, 'persons': persons}
	return render(request, 'home/house_gallery.html', args)

def castel_gallery(request):
	castels = Castel.objects.all()
	args = {'castels': castels}
	return render(request, 'home/castel_gallery.html', args)

def view_house(request, id=None):
	if id is not None:
		house = get_object_or_404(House, id=id)
		persons = Person.objects.filter(house__id=id)
		args = {'house': house, 'persons': persons}
		try:
			castel = get_object_or_404(Castel, owner_id=id)
			args['castel'] = castel
		except:
			pass
	else:
		return redirect('home:home')
	return render(request, 'home/view_house.html', args)

def view_profile(request, id=None):
	if id is not None:
		person = get_object_or_404(Person, id=id)
		args = {'person': person}
	else:
		return redirect('home:home')
	return render(request, 'home/view_person.html', args)

def view_castel(request, id=None):
	if id is not None:
		castel = get_object_or_404(Castel, id=id)
		args = {'castel': castel}
	else:
		return redirect('home:home')
	return render(request, 'home/view_castel.html', args)