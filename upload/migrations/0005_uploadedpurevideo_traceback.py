# Generated by Django 2.1.7 on 2019-03-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('upload', '0004_auto_20190314_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedpurevideo',
            name='traceback',
            field=models.TextField(blank=True, null=True, verbose_name='トレースバック'),
        ),
    ]
