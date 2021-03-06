# Generated by Django 3.0.4 on 2020-04-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0017_auto_20200406_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(choices=[('orange', 'orange'), ('orange-dark', 'orange-dark'), ('orange-light', 'orange-light'), ('yellow', 'yellow'), ('yellow-dark', 'yellow-dark'), ('yellow-light', 'yellow-light'), ('green', 'green'), ('green-dark', 'green-dark'), ('green-light', 'green-light'), ('turquoise', 'turquoise'), ('turquoise-dark', 'turquoise-dark'), ('turqoise-light', 'turqoise-light'), ('cyan', 'cyan'), ('cyan-dark', 'cyan-dark'), ('cyan-light', 'cyan-light'), ('blue', 'blue'), ('blue-dark', 'blue-dark'), ('blue-light', 'blue-light'), ('purple', 'purple'), ('purple-dark', 'purple-dark'), ('purple-light', 'purple-light'), ('red', 'red'), ('red-dark', 'red-dark'), ('red-light', 'red-light'), ('pink', 'pink'), ('pink-dark', 'pink-dark'), ('pink-light', 'pink-light'), ('grey', 'grey'), ('grey-dark', 'grey-dark'), ('grey-light', 'grey-light')], max_length=20, verbose_name='色'),
        ),
    ]
