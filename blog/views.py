from django.shortcuts import render
import datetime
from .models import Article
import markdown


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context=context)


def articles(request):
    articles = Article.objects.all()
    context = {
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
    article.content = markdown.markdown(article.content,
                                     extensions=[
                                         # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])
    context = {
        'article': article,
        'time': now
    }
    return render(request, 'blog/article_detail.html', context=context)
