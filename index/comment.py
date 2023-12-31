import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Comment
from .forms import CommentForm
from .views import get_user_ip, get_ip_attribution


def comments(request):
    comments = get_comments()
    author, email = get_user_data(request)
    comment_form = CommentForm(initial={'author': author, 'email': email})
    return render(request, 'index/comments.html', locals())

def add_comment(request):
    author, email = get_user_data(request)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            author = comment_form.cleaned_data['author']
            email = comment_form.cleaned_data['email']
            content = comment_form.cleaned_data['content']
            set_user_data(request, author, email)
            comment = Comment.objects.create()
            comment.author = author
            comment.email = email
            comment.content = content
            ip = get_user_ip(request)
            comment.ip = ip
            comment.ip_attribution = get_ip_attribution(ip)
            comment.save()
            sendTo(author)
            return HttpResponseRedirect(reverse('index:comments'))
        else:
            error = comment_form.errors.as_text
            comment_form = CommentForm(initial={'author': author, 'email': email})
    else:
        comment_form = CommentForm(initial={'author': author, 'email': email})
    comments = get_comments()
    return render(request, 'index/comments.html', locals())

def get_comments():
    comment_data = Comment.objects.filter(delete=False)
    comments = []
    for item in comment_data:
        if item.parent_id == 0:
            comments.append(item)
    for item in comment_data:
        for comment in comments:
            if item.parent_id == comment.id:
                comment.reply = item
    return comments

def get_user_data(request):
    author = request.session.get('author', '')
    email = request.session.get('email', '')
    return author, email

def set_user_data(request, author, email):
    request.session['author'] = author
    request.session['email'] = email

def sendTo(commentator):
    try:
        server_sender = "Pythonanywhere Admin<zhang.sihui@qq.com>"
        admin_receiver = "zhang_sihui@qq.com"
        subject = "Pythonanywhere Notice"
        body = f"{commentator} left you a message."

        msg = MIMEMultipart()  
        msg['Subject'] = subject
        msg['From'] = server_sender
        msg['To'] = admin_receiver
        msg.attach(MIMEText(body, 'plain'))  
        
        server_email = "zhang.sihui@qq.com"
        authorization_code = "umciyczdmlorjecg"
        server = smtplib.SMTP('smtp.qq.com')
        server.starttls()
        server.login(server_email, authorization_code)
        server.sendmail(server_sender, admin_receiver, msg.as_string())
        server.quit()
    except Exception as e:
        pass
