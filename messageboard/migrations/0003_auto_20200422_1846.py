# Generated by Django 2.1.3 on 2020-04-22 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20191130_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageboard',
            old_name='message',
            new_name='content',
        ),
    ]
