from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    context_object_name = 'article'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/delete.html'


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Form is invalid'

    form = ArticleForm()

    context = {
        'form' : form,
        'error' : error
    }

    return render(request, 'news/create.html', context)