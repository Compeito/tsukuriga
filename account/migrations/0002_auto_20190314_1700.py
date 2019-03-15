# Generated by Django 2.1.7 on 2019-03-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='プロフィール文'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_banner_url',
            field=models.URLField(blank=True, null=True, verbose_name='プロフィール背景画像URL'),
        ),
    ]