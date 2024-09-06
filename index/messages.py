from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Message
from .forms import MessageForm, initial_register_form, initial_login_form
from .views import get_user_ip, get_ip_attribution
from .common import translate_message


def messages(request):
    pathname = 'messages'
    messages = get_messages()
    message_form = MessageForm()
    login_form = initial_login_form(request)
    register_form = initial_register_form(request)
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
    return render(request, 'index/messages.html', locals())

def add_message(request):
    messages = get_messages()
    message_form = MessageForm()
    creator = request.session.get('username', '')
    if not creator:
        error_add_msg = translate_message("no login data")
        return render(request, 'index/messages.html', locals())
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            content = message_form.cleaned_data['content']
            message = Message.objects.create()
            message.creator = creator
            message.content = content
            ip = get_user_ip(request)
            message.ip_attribution = get_ip_attribution(ip)
            message.save()
            return HttpResponseRedirect(reverse('index:messages'))
        else:
            error_add_msg = message_form.errors.as_text().replace('content', translate_message('content'))
    return render(request, 'index/messages.html', locals())

def get_messages():
    message_data = Message.objects.filter(delete=False).order_by('-created_date')
    messages = []
    for item in message_data:
        if item.parent_id == 0:
            messages.append(item)
    for item in message_data:
        for message in messages:
            if item.parent_id == message.id:
                message.reply = item
    return messages
