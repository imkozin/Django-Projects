from django.urls import path
from .views import index, home, create

urlpatterns = [
    path('<int:pk>', index, name='index'),
    path('', home, name='home'),
    path('create/', create, name='create')
]