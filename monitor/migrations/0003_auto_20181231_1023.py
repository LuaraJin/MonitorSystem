# Generated by Django 2.1.4 on 2018-12-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20181228_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='date',
            field=models.DateTimeField(default=None, verbose_name='主机注册时间'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='date',
            field=models.DateTimeField(default=None, verbose_name='主机组注册时间'),
        ),
    ]
