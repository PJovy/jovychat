from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('articles/<int:article_id>', views.article_detail, name='article_detail'),
]
