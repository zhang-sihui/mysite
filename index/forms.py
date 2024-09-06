from django import forms
from .common import translate_message


class MessageForm(forms.Form):
    content = forms.CharField(label=translate_message('content'), max_length=512, 
                              widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}))

class LoginForm(forms.Form):
    username = forms.CharField(label=translate_message('username'), max_length=16,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=translate_message('password'), max_length=16,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label=translate_message('username'), max_length=16, min_length=1,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=translate_message('password'), max_length=16, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label=translate_message('confirm_password'), max_length=16, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=translate_message('email'), max_length=64, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

class CommentForm(forms.Form):
    content = forms.CharField(label=translate_message('content'), max_length=512, min_length=1,
                              widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}))

class ReplyForm(forms.Form):
    content = forms.CharField(label=translate_message('content'), max_length=512, min_length=1,
                              widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}))

def initial_register_form(request):
    register_username = request.session.get('register_username', '')
    register_eamil = request.session.get('register_eamil', '')
    initial_register_data = {}
    if register_username:
        initial_register_data['username'] = register_username
    if register_eamil:
        initial_register_data['eamil'] = register_eamil
    register_form = RegisterForm()
    if register_username or register_eamil:
        register_form = RegisterForm(initial=initial_register_data)
    return register_form

def initial_login_form(request):
    login_username = request.session.get('login_username', '')
    initial_login_data = {}
    if login_username:
        initial_login_data['username'] = login_username
    login_form = LoginForm()
    if login_username:
        login_form = LoginForm(initial=initial_login_data)
    return login_form
