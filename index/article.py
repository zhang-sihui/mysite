import json
import datetime
import markdown
from django.db.models import Min, Max, Prefetch
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .views import get_user_ip
from .models import Article, Category, Comment, Reply
from .forms import CommentForm, initial_register_form, initial_login_form
from .common import translate_message


def get_article_count_from_categorys():
    categorys = Category.objects.filter(delete=False).order_by('name')
    category_to_article_count = {}
    for category in categorys:
        articles_by_category = Article.objects.filter(category=category, status='pub')
        if articles_by_category:
            category_to_article_count[category.name] = len(articles_by_category)
    return category_to_article_count
    

def get_article_count_from_years():
    min_pub_date = Article.objects.aggregate(Min('pub_date'))['pub_date__min']
    min_pub_date_year = min_pub_date.year if min_pub_date else datetime.datetime.now().year
    max_pub_date = Article.objects.aggregate(Max('pub_date'))['pub_date__max']
    max_pub_date_year = max_pub_date.year if max_pub_date else datetime.datetime.now().year

    years_list = []
    for i in range(max_pub_date_year, min_pub_date_year - 1, -1):
        years_list.append(i)
    year_to_article_count = {}
    for year in years_list:
        articles_by_year = Article.objects.filter(pub_date__year=year, status='pub')
        if articles_by_year:
            year_to_article_count[year] = len(articles_by_year)
    return year_to_article_count

def articles(request):
    articles = Article.objects.filter(status='pub').order_by('-pub_date')
    category_to_article_count = get_article_count_from_categorys()
    year_to_article_count = get_article_count_from_years()
    return render(request, 'index/article.html', locals())


def article_body(request, article_id):
    article = get_object_or_404(Article, pk=int(article_id))
    article.views += 1
    article.latest_viewing_date = timezone.now()
    article.latest_viewing_user = get_user_ip(request)
    article.save()
    extensions = [ 'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc']
    article.body = markdown.markdown(article.body, extensions=extensions)
    category_to_article_count = get_article_count_from_categorys()
    year_to_article_count = get_article_count_from_years()
    # 获取指定文章下的所有评论及其回复
    comments = Comment.objects.filter(delete=False, article_id=article_id).prefetch_related(
            Prefetch('reply_set', queryset=Reply.objects.filter(delete=False))
        ).order_by('-created_date')
    comment_ids = []
    for comment in comments:
        comment_ids.append(comment.id)
    comments_id = json.dumps(comment_ids)
    login_form = initial_login_form(request)
    register_form = initial_register_form(request)
    comment_form = CommentForm()
    pathname = f'articles/{article_id}'
    # 密码不正确
    incorrect_password = request.session.pop('incorrect_password', False)
    if incorrect_password:
        login_error_msg = translate_message('The password is incorrect')
    # 用户不存在
    user_not_exist = request.session.pop('user_not_exist', False)
    if user_not_exist:
        login_error_msg = translate_message('User does not exist')
    # 注册成功
    register_success = request.session.pop('register_success', False)
    if register_success:
        login_info_msg = translate_message('register success')
    # 注册时用户存在
    user_exist = request.session.pop('user_exist', False)
    if user_exist:
        register_error_msg = translate_message('The user already exists, please modify the username')
    # 注册时不同的密码
    different_passwords = request.session.pop('different_passwords', False)
    if different_passwords:
        register_error_msg = translate_message('The passwords entered twice are different')
    # 注册时邮箱不正确
    invalid_email = request.session.pop('invalid_email', False)
    if invalid_email:
        register_error_msg = translate_message('valid email')
    return render(request, 'index/article_body.html', locals())


def get_search_articles(request):
    q = request.GET.get('q')
    articles = Article.objects.all().filter(status='pub').order_by('-pub_date')
    search_articles = Article.objects.filter(title__icontains=q, status='pub')
    search_articles_count = len(search_articles)
    success_search_msg = '{} results for {}'.format(search_articles_count, q)
    not_search_msg = 'No {} '.format(q)
    category_to_article_count = get_article_count_from_categorys()
    year_to_article_count = get_article_count_from_years()
    return render(request, 'index/search_articles.html', locals())


def get_articles_by_category(request, category):
    articles = Article.objects.filter(category=category, status='pub').order_by('-pub_date')
    category_to_article_count = get_article_count_from_categorys()
    year_to_article_count = get_article_count_from_years()
    return render(request, 'index/articles_by_category.html', locals())


def get_articles_by_year(request, year):
    articles = Article.objects.filter(pub_date__year=year, status='pub').order_by('-pub_date')
    category_to_article_count = get_article_count_from_categorys()
    year_to_article_count = get_article_count_from_years()
    return render(request, 'index/articles_by_year.html', locals())
