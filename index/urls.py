from django.urls import path
from . import views, article

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_site, name='about_site'),

    path('articles', article.articles, name='articles'),
    path('articles/<int:article_id>', article.article_body, name='article_body'),
    path('searchArticles', article.get_search_articles, name='get_search_articles'),
    path('articlesByLabel/<str:label>', article.get_articles_by_label, name='get_articles_by_label'),
    path('articlesByYear/<str:year>', article.get_articles_by_year, name='get_articles_by_year'),
]