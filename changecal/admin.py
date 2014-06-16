#admin.py

from django.contrib import admin
from changecal.models import ChangeRequest
from changecal.forms import ChangeRequestForm

class ChangeRequestAdmin(admin.ModelAdmin):
	form = ChangeRequestForm

	list_display = ('title', 'status')
	list_per_page = 50
	ordering = ['title']
	search_fields = ['title']


admin.site.register(ChangeRequest, ChangeRequestAdmin)

