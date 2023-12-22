import markdown
import json
import urllib.request
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone
from .models import UserIP, Visit, About

# Create your views here.

def index(request):
    user_ip = get_user_ip(request)
    if not check_ip(user_ip):
        add_ip(user_ip)
    today_visits = get_today_visit()
    if not today_visits:
        create_visit()
    today_visits = add_one_visit()
    total_visits = get_total_visit()
    localtime = timezone.now()
    return render(request, 'index/index.html', locals())


def add_one_visit():
    visit = Visit.objects.get(date=timezone.localdate())
    visit.visits += 1
    visit.save()
    return visit


def get_today_visit():
    visits = Visit.objects.filter(date=timezone.localdate())
    return visits


def create_visit():
    visit = Visit.objects.create()
    visit.save()


def get_total_visit():
    visits = Visit.objects.aggregate(Sum('visits'))
    return visits

def check_ip(user_ip):
    ip_data = UserIP.objects.filter(user_ip=user_ip)
    if ip_data:
        return True
    return False


def add_ip(user_ip):
    ips = UserIP.objects.all()
    ip_attribution = get_ip_attribution(user_ip)
    new_ip = UserIP.objects.create()
    new_ip.user_ip = user_ip
    new_ip.serial_number = len(ips) + 1
    new_ip.ip_attribution = ip_attribution
    new_ip.save()


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_ip_attribution(ip):
    apikey = '588481dc94e6ddc00d10947d57aa8e91'
    url = "http://api.tianapi.com/txapi/ipquery/index?key={}&ip={}".format(apikey, ip)
    req = urllib.request.urlopen(url)
    content = req.read().decode('utf-8')
    jsonResponse = json.loads(content)  # 将数据转化为 json 格式
    country, province, city, district, isp = '', '', '', '', ''
    if jsonResponse['code'] == 200:
        newslist = jsonResponse['newslist']
        country = newslist[0]['country'] if newslist[0]['country'] else ''
        province = newslist[0]['province'] if newslist[0]['province'] else ''
        city = newslist[0]['city'] if newslist[0]['city'] else ''
        district = newslist[0]['district'] if newslist[0]['district'] else ''
        isp = newslist[0]['isp'] if newslist[0]['isp'] else ''
    return (country + ' ' + province + ' ' + city + ' ' + district + ' ' + isp)


def about_site(request):
    # 返回日期最近的一条
    about_site = About.objects.all().order_by('-pub_date').first()
    if about_site:
        extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc']
        about_site.content = markdown.markdown(about_site.content, extensions=extensions)
    return render(request, 'index/about_site.html', locals())
