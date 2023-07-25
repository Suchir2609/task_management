from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, TaskUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in ')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


def index(request):
    return render(request, template_name='tasks/index.html')


def home(request):
    return render(request, 'tasks/home.html')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'assigned_team_member', 'priority']
    template_name = 'tasks/task_new.html'
    success_url = '/home'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


def task_status(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            messages.success(request, f'status has been changed')
            return redirect('home')
    else:
        form = TaskUpdateForm(instance=tasks)
    return render(request, 'tasks/task_status.html', {'form': form, 'tasks': tasks})


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/home'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator or self.request.user == task.assigned_team_member:
            return True
        return False


# def search(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         searched_priority = Task.objects.filter(priority=searched)
#         return render(request, 'tasks/search.html', {'searched': searched, 'searched_priority': searched_priority})
