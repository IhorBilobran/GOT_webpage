from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', )
	list_filter = ('house', 'created')
	ordering = ('user',)
	search_fields = ['user__username',]

admin.site.register(UserProfile, UserProfileAdmin)