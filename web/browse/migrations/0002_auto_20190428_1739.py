# Generated by Django 2.1.8 on 2019-04-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='day',
            field=models.CharField(choices=[('day', '24時間'), ('week', '週間'), ('month', '月間'), ('all', '全期間')],
                                   default=1, max_length=20, verbose_name='期間(日)'),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='type',
            field=models.CharField(choices=[('favorites', 'お気に入り順')], default='popular', max_length=20,
                                   verbose_name='集計タイプ'),
        ),
    ]
