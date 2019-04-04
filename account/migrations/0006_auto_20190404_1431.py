# Generated by Django 2.1.7 on 2019-04-04 05:31

import account.models
import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0005_auto_20190404_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='プロフィール文'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='表示名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_banner',
            field=models.ImageField(blank=True, default='images/default-banner.png', null=True,
                                    upload_to=account.models.profile_image_upload_to, verbose_name='プロフィール背景画像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_icon',
            field=models.ImageField(blank=True, default='images/default-icon.png', null=True,
                                    upload_to=account.models.profile_image_upload_to, verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, validators=[account.validators.UsernameValidator()],
                                   verbose_name='ユーザー名'),
        ),
    ]
