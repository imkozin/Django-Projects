from django.shortcuts import render

# Create your views here.
def index(request):

    data = {
        'title' : 'Homepage',
        'values' : ['Hello', 'this', 'is', 'website', 'on', 'django'],
        'obj' : {
            'car' : 'BMW',
            'age' : 29,
            'hobby' : 'programming'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')