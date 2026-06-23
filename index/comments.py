from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Comment
from .forms import CommentForm, initial_register_form, initial_login_form
from .views import get_user_ip, get_ip_attribution
from .common import translate_message


def messages(request):
    pathname = 'messages'
    messages = get_messages()
    message_form = CommentForm()
    login_form = initial_login_form(request)
    register_form = initial_register_form(request)
    incorrect_password = request.session.pop('incorrect_password', False)
    if incorrect_password:
        login_error_msg = translate_message('The password is incorrect')
    user_not_exist = request.session.pop('user_not_exist', False)
    if user_not_exist:
        login_error_msg = translate_message('User does not exist')
    register_success = request.session.pop('register_success', False)
    if register_success:
        login_info_msg = translate_message('register success')
    user_exist = request.session.pop('user_exist', False)
    if user_exist:
        register_error_msg = translate_message('The user already exists, please modify the username')
    different_passwords = request.session.pop('different_passwords', False)
    if different_passwords:
        register_error_msg = translate_message('The passwords entered twice are different')
    invalid_email = request.session.pop('invalid_email', False)
    if invalid_email:
        register_error_msg = translate_message('valid email')
    return render(request, 'index/messages.html', locals())


def add_message(request):
    messages = get_messages()
    message_form = CommentForm()
    creator = request.session.get('username', '')
    if not creator:
        error_add_msg = translate_message("no login data")
        return render(request, 'index/messages.html', locals())
    if request.method == 'POST':
        message_form = CommentForm(request.POST)
        if message_form.is_valid():
            content = message_form.cleaned_data['content']
            comment = Comment.objects.create()
            comment.creator = creator
            comment.content = content
            ip = get_user_ip(request)
            comment.ip_attribution = get_ip_attribution(ip)
            comment.save()
            return HttpResponseRedirect(reverse('index:messages'))
        else:
            error_add_msg = message_form.errors.as_text().replace('content', translate_message('content'))
    return render(request, 'index/messages.html', locals())


def get_messages():
    roots = Comment.objects.filter(article=None, root_id=0, delete=False).order_by('-create_date')
    root_ids = roots.values_list('id', flat=True)
    replies = Comment.objects.filter(article=None, root_id__in=root_ids, delete=False)
    reply_map = {r.root_id: r for r in replies}
    for root in roots:
        if root.id in reply_map:
            root.reply = reply_map[root.id]
    return list(roots)


def add_comment(request, article_id):
    creator = request.session.get('username', '')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            comment = Comment.objects.create()
            comment.creator = creator
            comment.content = content
            comment.article_id = article_id
            ip = get_user_ip(request)
            comment.ip_attribution = get_ip_attribution(ip)
            comment.save()
            return redirect(f'/articles/{article_id}')
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return redirect(f'/articles/{article_id}')


def add_reply(request, pathname):
    creator = request.session.get('username', '')
    path_data = pathname[1:-1].split('&')
    if path_data[1] == 'comment':
        parent = Comment.objects.get(id=path_data[0])
        root_id = parent.id
        reply_to_id = parent.id
        reply_to_creator = parent.creator
        article = parent.article
    elif path_data[1] == 'reply':
        parent = Comment.objects.get(id=path_data[0])
        root_id = parent.root_id
        reply_to_id = parent.id
        reply_to_creator = parent.creator
        root = Comment.objects.get(id=root_id)
        article = root.article
    if request.method == 'POST':
        reply_form = CommentForm(request.POST)
        if reply_form.is_valid():
            content = reply_form.cleaned_data['content']
            comment = Comment.objects.create()
            comment.creator = creator
            comment.content = content
            comment.article = article
            comment.root_id = root_id
            comment.reply_to_id = reply_to_id
            comment.reply_to_creator = reply_to_creator
            ip = get_user_ip(request)
            comment.ip_attribution = get_ip_attribution(ip)
            comment.save()
            return redirect(f'/articles/{article.id}')
        else:
            reply_form = CommentForm()
    else:
        reply_form = CommentForm()
    return redirect(f'/articles/{article.id}')
