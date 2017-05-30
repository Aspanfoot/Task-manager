from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from .models import Task
from .forms import TaskForm, ShareForm
from django.contrib.auth.models import User

# Create your views here.

def profile(request):
	
	return render(request, 'user_profile/profile.html')

def tasks(request):
	data = dict()
	tasks = Task.objects.filter(user__id = request.user.id)
	context = {
		'tasks': tasks
	}
	if request.is_ajax():
		data['html_task_list'] = render_to_string('user_profile/add_task_list.html', context)
		return JsonResponse(data)

	return render(request, 'user_profile/tasks.html', context)


def save_task_form(request, form, template_name):
	data = dict()
	if request.method =='POST':
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.host = "Me"
			obj.save()
			data['form_is_valid'] = True
			tasks = Task.objects.filter(user__id = request.user.id)
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
		tasks = Task.objects.filter(user__id = request.user.id)
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

def share_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	data = dict()

	if request.method == 'POST':
		form = ShareForm(request.POST)
		if form.is_valid():
			#Very very bad practice, jast hardcoding
			#while tests are not done. You can have like multiple users etc 
			#so its gona take time to get this emails.
			#English comment bcs of python 2
			email = form.cleaned_data["email"]
			#All of this should be form errors
			if email not in User.objects.all().values_list('email', flat = True):
				# Could be UserDoesNotExist built in django exception
				raise Exception("User doesnt exist")
			elif email == request.user.email:
				raise Exception("Sharing task with yourself.")

			user = User.objects.get(email = email)
			task.host = request.user.username
			task.user = user
			task.pk = None
			task.save()

			data['form_is_valid'] = True
		else:
			data['form_is_valid'] = False
	else:
		form = ShareForm()

	tasks = Task.objects.filter(user__id = request.user.id)
	data['html_task_list'] = render_to_string('user_profile/add_task_list.html', {
			'tasks': tasks
		})
	context = {'form': form, 'task':task}
	data['html_form'] = render_to_string('user_profile/share_task.html', context, request = request)

	return JsonResponse(data)