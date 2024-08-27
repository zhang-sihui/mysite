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
