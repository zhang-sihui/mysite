from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from .common import translate_message

# Create your models here.

class About(models.Model):
    title = models.CharField(translate_message('title'), max_length=20)
    pub_date = models.DateTimeField(translate_message('pub_date'), default=timezone.now)
    content = MDTextField(translate_message('content'))


class UserIP(models.Model):
    user_ip = models.CharField(translate_message('user_ip'), max_length=20)
    serial_number = models.CharField(translate_message('serial_number'), max_length=10, default=0)
    access_time = models.DateTimeField(translate_message('access_time'), default=timezone.now)
    ip_attribution = models.CharField(translate_message('ip_attribution'), max_length=64, default='')


class Visit(models.Model):
    date = models.DateField(translate_message('date'), default=timezone.localdate)
    visits = models.IntegerField(translate_message('visits'), default=0)
    first_viewing_ip = models.CharField(translate_message('first_viewing_ip'), max_length=16, default='')
    latest_viewing_ip = models.CharField(translate_message('latest_viewing_ip'), max_length=16, default='')


class Author(models.Model):
    name = models.CharField(translate_message('author'), max_length=16, default='', unique=True)
    created_date = models.DateTimeField(translate_message('created_date'), default=timezone.now)
    delete = models.BooleanField(translate_message('delete'), default=False)

    def __str__(self):
        return self.name    


class Category(models.Model):
    name = models.CharField(translate_message('category'), max_length=16, default='', unique=True)
    created_date = models.DateTimeField(translate_message('created_date'), default=timezone.now)
    delete = models.BooleanField(translate_message('delete'), default=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Status', max_length=16, default='', unique=True)
    name_cn = models.CharField(translate_message('status'), max_length=16, default='', unique=True)
    created_date = models.DateTimeField(translate_message('created_date'), default=timezone.now)
    delete = models.BooleanField(translate_message('delete'), default=False)

    def get_chinese_name(self):
        return self.name_cn

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(translate_message('title'), max_length=200)
    author = models.CharField(translate_message('author'), max_length=16, default='')
    _author = models.ForeignKey(Author, on_delete=models.CASCADE, limit_choices_to={'delete': False}, null=True, verbose_name=translate_message('author'))
    category = models.CharField(translate_message('category'), max_length=10, default='')
    _category = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={'delete': False},  null=True, verbose_name=translate_message('category'))
    body = MDTextField(translate_message('content'))
    pub_date = models.DateTimeField(translate_message('pub_date'), default=timezone.now)
    views = models.IntegerField(translate_message('views'), default=0)
    mod_date = models.DateTimeField(translate_message('mod_date'), default=timezone.now)
    status = models.CharField(translate_message('status'), max_length=8, default='')
    _status = models.ForeignKey(Status, on_delete=models.CASCADE, limit_choices_to={'delete': False}, null=True, verbose_name=translate_message('status'))
    latest_viewing_date = models.DateTimeField(translate_message('latest_viewing_date'), default=timezone.now)
    latest_viewing_user = models.CharField(translate_message('latest_viewing_user'), max_length=16, default='')

    def save(self, *args, **kwargs):
        if self._author:
            author_object = Author.objects.get(name=self._author)
            self.author = author_object.name
        if self._category:
            category_object = Category.objects.get(name=self._category)
            self.category = category_object.name
        if self._status:
            status_object = Status.objects.get(name=self._status)
            self.status = status_object.name
        super(Article, self).save(*args, **kwargs)

class File(models.Model):
    file_name = models.CharField(translate_message('file_name'), max_length=100)
    file_size = models.IntegerField(translate_message('file_size'), default=0)
    pub_date = models.DateTimeField(translate_message('pub_date'), default=timezone.now)
    downloads = models.IntegerField(translate_message('downloads'), default=0)

class Message(models.Model):
    creator = models.CharField(translate_message('creator'), max_length=16)
    content = models.TextField(translate_message('content'), max_length=512)
    ip_attribution = models.CharField(translate_message('ip_attribution'), max_length=64, default='', blank=True, null=True)
    parent_id = models.IntegerField(translate_message('parent_id'), default=0)
    created_date = models.DateTimeField(translate_message('created_date'), default=timezone.now)
    delete = models.BooleanField(translate_message('delete'), default=False)

class User(models.Model):
    username = models.CharField(translate_message('username'), max_length=16, blank=True, unique=True)
    password = models.CharField(translate_message('password'), max_length=16, blank=True)
    email = models.CharField(translate_message('email'), max_length=64, default='', blank=True, null=True)
    created_date = models.DateTimeField(translate_message('created_date'), default=timezone.now)
    delete = models.BooleanField(translate_message('delete'), default=False)
