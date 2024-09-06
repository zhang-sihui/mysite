from django.shortcuts import redirect
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
from .views import get_user_ip, get_ip_attribution
from .common import translate_message

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
            error_add_msg = comment_form.errors.as_text().replace('content', translate_message('content'))
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return redirect(f'/articles/{article_id}')

def add_reply(request, pathname):
    creator = request.session.get('username', 'A')
    path_data = pathname[1:-1].split('&')
    if path_data[1] == 'comment':
        comment_id = path_data[0]
        comment = Comment.objects.get(id=comment_id)
        receiver = comment.creator
    elif path_data[1] == 'reply':
        reply_id = path_data[0]
        reply = Reply.objects.get(id=reply_id)
        comment = reply.comment
        receiver = reply.creator
    article_id = comment.article_id
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            content = reply_form.cleaned_data['content']
            reply = Reply.objects.create()
            reply.creator = creator
            reply.content = content
            reply.comment = comment
            reply.receiver = receiver
            ip = get_user_ip(request)
            reply.ip_attribution = get_ip_attribution(ip)
            reply.save()
            return redirect(f'/articles/{article_id}')
        else:
            error_add_msg = reply_form.errors.as_text().replace('content', translate_message('content'))
            reply_form = ReplyForm()
    else:
        reply_form = ReplyForm()
    return redirect(f'/articles/{article_id}')
