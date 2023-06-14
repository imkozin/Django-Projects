import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    appid = 'b9d80c861c1073cb4293964e9f97d58a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : res['main']['temp'],
            'humidity' : res['main']['humidity']
        }

        all_cities.append(city_info)



    context = {
        'all_info' : all_cities,
        'form' : form
    }

    return render(request, 'weather/index.html', context)

