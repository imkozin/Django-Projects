from django.urls import path
from .views import index, about, create, delete, update, show_task

urlpatterns = [
    path('', index, name='home'),
    path('show/<int:pk>', show_task, name='task-detail'),
    path('about-us', about, name='about'),
    path('create', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update,
    name='update')
]