# Generated by Django 2.1.3 on 2020-05-02 21:09

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200423_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=16, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default='其他', max_length=10, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
