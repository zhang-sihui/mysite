import datetime
import markdown
from django.db.models import Min, Max
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .views import get_user_ip
from .models import Article, Category


def get_article_count_from_categorys():
    categorys = Category.objects.filter(delete=False)
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

    years_set = set()
    for i in range(min_pub_date_year, max_pub_date_year + 1):
        years_set.add(i)
    year_to_article_count = {}
    for year_set in years_set:
        articles_by_year = Article.objects.filter(pub_date__year=year_set, status='pub')
        if articles_by_year:
            year_to_article_count[year_set] = len(articles_by_year)
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
