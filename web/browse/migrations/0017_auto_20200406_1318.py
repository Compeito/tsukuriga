# Generated by Django 3.0.4 on 2020-04-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0016_label_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='icon',
            field=models.CharField(default='fas fa-star', max_length=50, verbose_name='アイコン'),
        ),
    ]