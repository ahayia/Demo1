# Generated by Django 3.0.8 on 2020-09-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20200713_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gpic',
            field=models.ImageField(upload_to='static/df_goods', verbose_name='关联图片目录'),
        ),
    ]