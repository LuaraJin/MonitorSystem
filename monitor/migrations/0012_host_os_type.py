# Generated by Django 2.1.4 on 2019-01-07 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_task_tasklogdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='os_type',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='系统类型'),
        ),
    ]
