# Generated by Django 4.2.7 on 2023-12-21 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_comment_delete'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutSite',
            new_name='About',
        ),
    ]