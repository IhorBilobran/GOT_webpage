from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', )
	list_filter = ('house', 'created')
	ordering = ('user',)
	search_fields = ['user__username',]

admin.site.register(Profile, ProfileAdmin)
