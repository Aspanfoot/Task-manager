from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from .models import Task
from .forms import TaskForm

# Create your views here.

def profile(request):
	
	return render(request, 'user_profile/profile.html')

def tasks(request):
	tasks = Task.objects.all()

	context = {
		'tasks': tasks
	}

	return render(request, 'user_profile/tasks.html', context)


def save_task_form(request, form, template_name):
	data = dict()

	if request.method =='POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			tasks = Task.objects.all()
			data['html_task_list'] = render_to_string('user_profile/add_task_list.html', {
				'tasks': tasks
			})
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request = request)

	return JsonResponse(data)

def add_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
	else:
		form = TaskForm()

	return save_task_form(request, form, 'user_profile/add_task.html')

def update_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
	else:
		form = TaskForm(instance=task)
	return save_task_form(request, form, 'user_profile/update_task.html')


def delete_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	data = dict()
	if request.method == 'POST':
		task.delete()
		data['form_is_valid'] = True
		tasks = Task.objects.all()
		data['html_task_list'] = render_to_string('user_profile/add_task_list.html', {
			'tasks': tasks
		})
	else:
		context = {'task': task}
		data['html_form'] = render_to_string('user_profile/delete_task.html', 
			context,
			request=request,
		)
	return JsonResponse(data)