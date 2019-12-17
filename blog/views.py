from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .models import Article, ArticleSection
import markdown
from .forms import ArticleForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context=context)


def articles(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    if search:
        if order == 'total_views':
            article_list = Article.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = Article.objects.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
    else:
        search = ''
        if order == 'total_views':
            article_list = Article.objects.all().order_by('-total_views')
        else:
            article_list = Article.objects.all().order_by('-pub_date')

    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        'articles': articles,
        'order': order,
        'search': search,
    }
    return render(request, 'blog/articles.html', context=context)


def about(request):
    now = datetime.datetime.now()
    context = {
        'time': now,
    }
    return render(request, 'blog/about.html', context=context)


def resume(request):
    try:
        article = Article.objects.get(title='Resume')
        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                # 包含 缩写、表格等常用扩展
                                                'markdown.extensions.extra',
                                                # 语法高亮扩展
                                                'markdown.extensions.codehilite',
                                            ])
        context = {
            'article': article
        }
        return render(request, 'blog/resume.html', context=context)
    except ObjectDoesNotExist as e:
        return HttpResponse(e)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    now = datetime.datetime.now()
    article.total_views += 1
    article.save(update_fields=['total_views'])
    md = markdown.Markdown(
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            # 目录拓展 Table of Contents
            'markdown.extensions.toc'
        ])
    article.content = md.convert(article.content)
    toc = md.toc
    context = {
        'article': article,
        'toc': toc,
    }
    return render(request, 'blog/article_detail.html', context=context)


@login_required(login_url='userprofile:login')
def article_create(request):
    if request.method == 'POST':
        article_post_form = ArticleForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            if request.POST['section'] != 'none':
                new_article.section = ArticleSection.objects.get(id=request.POST['section'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect('blog:articles')
        else:
            return HttpResponse("提交有误，请重新提交。")
    else:
        article_post_form = ArticleForm()
        sections = ArticleSection.objects.all()
        context = {
            'article_post_form': article_post_form,
            'sections': sections
        }
        return render(request, 'blog/article_create.html', context=context)


@login_required(login_url='userprofile:login')
def article_delete(request, article_id):
    article_to_delete = Article.objects.get(id=article_id)
    article_to_delete.delete()
    return redirect('blog:articles')


@login_required(login_url='userprofile:login')
def article_update(request, article_id):
    article_to_update = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article_post_form = ArticleForm(data=request.POST, instance=article_to_update)
        if article_post_form.is_valid():
            article_post_form.save()
            if request.POST['section'] != 'none':
                article_to_update.section = ArticleSection.objects.get(id=request.POST['section'])
            article_to_update.save()
            return redirect('blog:article_detail', article_id=article_to_update.id)
        else:
            return HttpResponse("Update error.")
    else:
        sections = ArticleSection.objects.all()
        context = {
            'article': article_to_update,
            'sections': sections
        }
        return render(request, 'blog/article_update.html', context=context)
