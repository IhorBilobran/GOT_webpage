from django.contrib import admin

from .models import House, Person, Castel

class HouseAdmin(admin.ModelAdmin):
	list_display = ('name', 'words',)
	ordering = ('name', )
	search_fields = ['name',]

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'house')
	list_filter = ('house', 'aliwe')
	ordering = ('name', )
	search_fields = ['name',]

class CastelAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner')
	ordering = ('name', )
	search_fields = ['name',]

admin.site.register(House, HouseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Castel, CastelAdmin)