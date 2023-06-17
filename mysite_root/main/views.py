from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.

def index(request, pk):
    ls = TodoList.objects.get(id=pk)
   
    if request.method == 'POST':
        if request.POST.get('save'):
            for item in ls.items.all():
                if request.POST.get('c' + str(item.id)) == 'clicked':
                    item.complete = True
                else:
                    item.complete = False

        elif request.POST.ge('newItem'):
            txt = request.POST.get('new')

            if len(txt) > 2:
                ls.items.create(text=txt, complete=False)
            else:
                print('invalid')

    return render(request, 'main/list.html', {'ls' : ls})

def home(request):
    return render(request, 'main/home.html', {})

def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = TodoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(request, 'main/home.html', {'form' : form})