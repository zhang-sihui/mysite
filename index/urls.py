from django.urls import path, re_path
from . import views, article, file, messages, users, comments

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    # 文章
    path('articles', article.articles, name='articles'),
    path('articles/<int:article_id>', article.article_body, name='article_body'),
    path('searchArticles', article.get_search_articles, name='get_search_articles'),
    path('articlesByCategory/<str:category>', article.get_articles_by_category, name='get_articles_by_category'),
    path('articlesByYear/<str:year>', article.get_articles_by_year, name='get_articles_by_year'),
    # 评论
    path('add_comment/<int:article_id>', comments.add_comment, name='add_comment'),
    # 回复
    re_path('add_reply/(?P<pathname>[\\a-zA-Z0-9]*)/', comments.add_reply, name='add_reply'),
    # 留言
    path('messages', messages.messages, name='messages'),
    path('add_message', messages.add_message, name='add_message'),
    # 文件
    path('files', file.files, name='files'),
    path('upload', file.upload, name='upload'),
    re_path('download/(?P<file_id>\\d+)/', file.download, name='download'),
    re_path('download_file/(?P<file_id>\\d+)/', file.download_file, name='download_file'),
    # 登录
    re_path('login/(?P<pathname>[\\a-zA-Z0-9]*)/', users.login, name='login'),
    re_path('register/(?P<pathname>[\\a-zA-Z0-9]*)/', users.register, name='register'),
    re_path('logout/(?P<pathname>[\\a-zA-Z0-9]*)/', users.logout, name='logout'),
]
