# Generated by Django 2.1.8 on 2019-04-30 08:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0008_auto_20190429_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoprofile',
            name='channels',
        ),
    ]