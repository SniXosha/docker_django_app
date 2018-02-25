from django.urls import path

from . import views

app_name = 'todotask'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('create/', views.create_task, name='create'),
    path('create/post', views.create_task_post, name='create_post'),
    path('<int:task_id>/finish', views.mark_as_finished, name='finish')
]