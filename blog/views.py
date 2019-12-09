from django.shortcuts import render
import datetime
from .models import Article


def home(request):
    now = datetime.datetime.now()
    articles = Article.objects.all()
    context = {
        'time': now,
        'articles': articles
    }
    return render(request, 'blog/home.html', context=context)


def articles(request):
    now = datetime.datetime.now()
    articles = Article.objects.all()
    context = {
        'time': now,
        'articles': articles
    }
    return render(request, 'blog/articles.html', context=context)


def about(request):
    now = datetime.datetime.now()
    context = {
        'time': now,
    }
    return render(request, 'blog/about.html', context=context)


def resume(request):
    now = datetime.datetime.now()
    context = {
        'time': now,
    }
    return render(request, 'blog/resume.html', context=context)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    now = datetime.datetime.now()
    context = {
        'article': article,
        'time': now
    }
    return render(request, 'blog/article_detail.html', context=context)
