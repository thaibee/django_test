# Generated by Django 3.2.10 on 2021-12-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20211230_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]