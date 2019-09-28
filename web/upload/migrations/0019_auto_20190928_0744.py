# Generated by Django 2.1.11 on 2019-09-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0018_video_is_pickup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='is_active',
        ),
        migrations.AddField(
            model_name='videoprofile',
            name='release_type',
            field=models.CharField(choices=[('published', '公開'), ('limited', '限定公開'), ('unpublished', '未公開')],
                                   default='unpublished', max_length=20, verbose_name='公開状態'),
        ),
    ]
