from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import generic
from django.utils import timezone

from .models import Task

LOGIN_URL = '/accounts/login'

@login_required(login_url=LOGIN_URL)
def index(request):
    relevant = Task.objects.order_by('-pub_date').filter(user=request.user, finished=False, deadline__gt=timezone.now())
    outdated = Task.objects.order_by('-pub_date').filter(user=request.user, finished=False, deadline__lt=timezone.now())
    finished = Task.objects.order_by('-pub_date').filter(user=request.user, finished=True)
    return render(request, 'todotask/index.html', {'relevant_tasks': relevant,
                                                   'outdated_tasks': outdated,
                                                   'finished_tasks': finished,})

class Detail(LoginRequiredMixin, generic.DetailView):
    login_url = LOGIN_URL

    model = Task
    template_name = 'todotask/detail.html'

@login_required(login_url=LOGIN_URL)
def create_task(request):
    return render(request, 'todotask/create.html', {})

@login_required(login_url=LOGIN_URL)
def create_task_post(request):
    new_task = Task(user=request.user)
    new_task.task_text = request.POST['task_text']
    if request.POST['deadline'] != '':
        new_task.deadline = request.POST['deadline']
    new_task.save()
    return HttpResponseRedirect(reverse('todotask:index'))

@login_required(login_url=LOGIN_URL)
def mark_as_finished(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.finished = True
    task.save()
    return HttpResponseRedirect(reverse('todotask:index'))