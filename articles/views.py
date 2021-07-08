from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {
        'articles': articles
    })

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/artical_detail.html', {
        'article': article
    }) 

@login_required()
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/artical_create.html', {
        'form': form
    })
