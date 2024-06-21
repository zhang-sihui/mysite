from django.urls import path, re_path
from . import views, article, comment, file

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_site, name='about_site'),

    path('articles', article.articles, name='articles'),
    path('articles/<int:article_id>', article.article_body, name='article_body'),
    path('searchArticles', article.get_search_articles, name='get_search_articles'),
    path('articlesByLabel/<str:label>', article.get_articles_by_label, name='get_articles_by_label'),
    path('articlesByYear/<str:year>', article.get_articles_by_year, name='get_articles_by_year'),

    path('comments', comment.comments, name='comments'),
    path('add_comment', comment.add_comment, name='add_comment'),
    # 文件
    path('files', file.files, name='files'),
    path('upload', file.upload, name='upload'),
    re_path('download/(?P<file_id>\\d+)/', file.download, name='download'),
    re_path('download_file/(?P<file_id>\\d+)/', file.download_file, name='download_file'),
]
