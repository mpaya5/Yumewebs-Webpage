# Generated by Django 3.1.7 on 2021-04-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210423_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Url del sitio web'),
        ),
    ]
