from django import forms
from manageconfig.models import ConfigurationItem, Manufacturer

class ConfigurationItemForm(forms.ModelForm):
	class Meta:
		model = ConfigurationItem

class ManufacturerForm(forms.ModelForm):
	class Meta:
		model = Manufacturer
