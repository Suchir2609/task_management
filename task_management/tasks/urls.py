from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('task_status/<int:pk>', views.task_status, name='task-status'),
    path('task_delete/<int:pk>', views.TaskDeleteView.as_view(), name='task-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tasks/logout.html'), name='logout'),
    path('home/', views.TaskListView.as_view(), name='home'),
    path('task_new', views.TaskCreateView.as_view(), name='task-new'),
    # path('search/', views.search, name='search'),
]

