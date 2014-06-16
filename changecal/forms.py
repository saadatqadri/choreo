from django import forms
from changecal.models import ChangeRequest

class ChangeRequestForm(forms.ModelForm):
	class Meta:
		model = ChangeRequest
