from django import forms
from .common import translate_message


class CommentForm(forms.Form):
    author = forms.CharField(label=translate_message('name'), 
                             max_length=16, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=translate_message('email'), 
                             max_length=64, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    content = forms.CharField(label=translate_message('content'), 
                              max_length=256, 
                              widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}))
