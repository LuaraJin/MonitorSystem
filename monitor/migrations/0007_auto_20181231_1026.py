# Generated by Django 2.1.4 on 2018-12-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20181231_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='主机注册时间'),
        ),
        migrations.AlterField(
            model_name='hostgroup',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='主机组注册时间'),
        ),
    ]
