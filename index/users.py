from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User

def login(request, pathname):
    """ 用户登录 """
    # 已登录用户不能登录
    if request.session.get('logged', False):
        return redirect(f'index:{pathname}')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user_data = User.objects.get(username=username)
                if user_data.password == password:
                    request.session['logged'] = True
                    request.session['id'] = user_data.id
                    request.session['username'] = user_data.username
                    return redirect(f'index:{pathname}')
                else:
                    request.session['incorrect_password'] = True
            except:
                request.session['user_not_exist'] = True
        return redirect(f'index:{pathname}')

def logout(request, pathname):
    """ 用户退出 """
    # pathname 代表退出的当前页面
    # flush()方法是比较安全的一种做法, 一次性将 session 中的所有内容全部清空
    if pathname in '/searchArticles':
        pathname = '/articles'
    if pathname in '/add_message':
        pathname = '/messages'
    request.session.flush()
    if not pathname.startswith('/'):
        pathname = '/' + pathname
    return redirect(f'{pathname}')

def register(request, pathname):
    """ 用户注册 """
    # 已登录用户不能注册
    if request.session.get('logged', False):
        return redirect(f'index:{pathname}')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            confirm_password = register_form.cleaned_data['confirm_password']
            if password != confirm_password:
                request.session['different_passwords'] = True
                return redirect(f'index:{pathname}')
            else:
                user = User.objects.filter(username=username)
                if user:
                    request.session['user_exist'] = True
                    return redirect(f'index:{pathname}')
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = password
                new_user.save()
                request.session['register_success'] = True
                return redirect(f'index:{pathname}')
        return render(request, 'index/register.html', locals())
    return redirect(f'index:{pathname}')
