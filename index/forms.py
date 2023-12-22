from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(label='名称', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    content = forms.CharField(label='评论', max_length=256, widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}))
