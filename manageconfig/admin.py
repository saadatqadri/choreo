#admin.py

from django.contrib import admin
from manageconfig.models import ConfigurationItem, Manufacturer
from manageconfig.forms import ConfigurationItemForm, ManufacturerForm

class ConfigurationItemAdmin(admin.ModelAdmin):
	form = ConfigurationItemForm

	list_display = ('title', 'status')
	list_per_page = 50
	ordering = ['title']
	search_fields = ['title']

admin.site.register(ConfigurationItem, ConfigurationItemAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
	form = ManufacturerForm

	list_display = ('name',)
	list_per_page = 50
	ordering = ['name']
	search_fields = ['name']

admin.site.register(Manufacturer, ManufacturerAdmin)
