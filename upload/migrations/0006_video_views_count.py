# Generated by Django 2.1.7 on 2019-03-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0005_uploadedpurevideo_traceback'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='再生回数'),
        ),
    ]
