from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from .models import House, Person, Castel
from accounts.models import Profile


def home(request):
	return render(request, 'home/home.html')

def house_gallery(request):
	houses = House.objects.all().order_by('name')
	persons = Person.objects.all()
	args = {'houses': houses, 'persons': persons}
	return render(request, 'home/house_gallery.html', args)

def castel_gallery(request):
	castels = Castel.objects.all()
	args = {'castels': castels}
	return render(request, 'home/castel_gallery.html', args)

def people_gallery(request):
	persons = Person.objects.all().order_by('name')
	args = {'persons': persons}
	return render(request, 'home/people_gallery.html', args)

def view_house(request, id=None):
	if id is not None:
		house = get_object_or_404(House, id=id)
		persons = Person.objects.filter(house__id=id)
		users = User.objects.filter(profile__house__id=id)

		args = {'house': house, 'persons': persons, 'users': users}
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
	return render(request, 'home/view_castel.html',args)

def give_pdf(request):
	# create the HttpResponse object with the appropriate PDF header
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="file.pdf"'

	# create pdf objects, using the response object
	p = canvas.Canvas(response)

	# Draw things on the PDF, here`s where the PDF generation happens
	# see ReportLab documentation for the full llist of functionality
	p.drawString(100, 100, 'hello world')

	#close pdf obj
	p.showPage()
	p.save()
	return response
