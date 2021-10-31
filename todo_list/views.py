from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'


class TaskAdd(CreateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('list')
    template_name_suffix = '_add'


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'
