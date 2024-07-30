from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class About(models.Model):
    title = models.CharField('标题', max_length=20)
    pub_date = models.DateTimeField('发布时间', default=timezone.now)
    content = MDTextField('内容')


class UserIP(models.Model):
    user_ip = models.CharField('用户ip', max_length=20)
    serial_number = models.CharField('访问序号', max_length=10, default=0)
    access_time = models.DateTimeField('首次访问时间', default=timezone.now)
    ip_attribution = models.CharField('ip地址', max_length=64, default='')


class Visit(models.Model):
    date = models.DateField('日期', default=timezone.localdate)
    visits = models.IntegerField('访问量', default=0)
    first_viewing_ip = models.CharField('首次访问ip', max_length=16, default='')
    latest_viewing_ip = models.CharField('最新访问ip', max_length=16, default='')


class Author(models.Model):
    name = models.CharField('作者', max_length=16, default='', unique=True)
    created_date = models.DateTimeField('创建日期', default=timezone.now)
    delete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.name    


class Category(models.Model):
    name = models.CharField('分类', max_length=16, default='', unique=True)
    created_date = models.DateTimeField('创建日期', default=timezone.now)
    delete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Status', max_length=16, default='', unique=True)
    name_cn = models.CharField('状态', max_length=16, default='', unique=True)
    created_date = models.DateTimeField('创建日期', default=timezone.now)
    delete = models.BooleanField('删除', default=False)

    def get_chinese_name(self):
        return self.name_cn

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('文章标题', max_length=200)
    author = models.CharField('作者', max_length=16, default='')
    _author = models.ForeignKey(Author, on_delete=models.CASCADE, limit_choices_to={'delete': False}, null=True, verbose_name='作者')
    category = models.CharField('分类', max_length=10, default='')
    _category = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={'delete': False},  null=True, verbose_name='分类')
    body = MDTextField('内容')
    pub_date = models.DateTimeField('发布日期', default=timezone.now)
    views = models.IntegerField('浏览量', default=0)
    mod_date = models.DateTimeField('修改时间', default=timezone.now)
    status = models.CharField('状态', max_length=8, default='')
    _status = models.ForeignKey(Status, on_delete=models.CASCADE, limit_choices_to={'delete': False}, null=True, verbose_name='状态')
    latest_viewing_date = models.DateTimeField('最新查看日期', default=timezone.now)
    latest_viewing_user = models.CharField('最新查看用户', max_length=16, default='')

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


class Comment(models.Model):
    author = models.CharField('作者', max_length=16, default='')
    email = models.CharField('邮箱', max_length=64, default='', blank=True, null=True)
    content = MDTextField('内容')
    sub_date = models.DateTimeField('创建日期', default=timezone.now)
    ip = models.CharField('用户IP', max_length=16, default='', blank=True, null=True)
    ip_attribution = models.CharField('IP地址', max_length=64, default='', blank=True, null=True)
    parent_id = models.IntegerField('连接对象', default=0)
    delete = models.BooleanField('删除', default=False)

class File(models.Model):
    file_name = models.CharField('文件名', max_length=100)
    file_size = models.IntegerField('文件大小', default=0)
    pub_date = models.DateTimeField('上传日期', default=timezone.now)
    downloads = models.IntegerField('下载数', default=0)
