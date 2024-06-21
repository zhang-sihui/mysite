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


class Article(models.Model):
    states = (
        ('draft', '草稿'),
        ('pub', '发布'),
    )
    title = models.CharField('文章标题', max_length=200)
    author = models.CharField('作者', max_length=16)
    category = models.CharField('分类', max_length=10, default='其他')
    body = MDTextField('内容')
    pub_date = models.DateTimeField('发布日期', default=timezone.now)
    views = models.IntegerField('浏览量', default=0)
    mod_date = models.DateTimeField('修改时间', default=timezone.now)
    state = models.CharField('状态', max_length=8, choices=states, default='draft')
    latest_viewing_date = models.DateTimeField('最新查看日期', default=timezone.now)
    latest_viewing_user = models.CharField('最新查看用户', max_length=16, default='')

    def __str__(self):
        return self.title

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
