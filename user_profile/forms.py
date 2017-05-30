from django import forms
from django.forms import Textarea
from . models import Task


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		exclude = ('user', 'host',)
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3,
										   'style' :'resize:none;'}),
		}

class ShareForm(forms.Form):
	label = "Email"
	email = forms.EmailField(label = label, required=True)