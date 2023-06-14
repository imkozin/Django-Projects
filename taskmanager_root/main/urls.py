from django.urls import path
from .views import index, about, create, delete

urlpatterns = [
    path('', index, name='home'),
    path('about-us', about, name='about'),
    path('create', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete')
]