# Generated by Django 3.1.7 on 2021-04-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210419_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Url del sitio web'),
        ),
    ]
