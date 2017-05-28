from django import forms
from django.forms import Textarea
from . models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3,
										   'style' :'resize:none;'}),
		}
