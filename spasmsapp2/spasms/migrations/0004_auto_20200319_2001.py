# Generated by Django 3.0.3 on 2020-03-19 20:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spasms', '0003_auto_20200319_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='hashtags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spasms.HashTag'),
        ),
        migrations.AlterField(
            model_name='tweetrun',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 19, 20, 1, 47, 18290)),
        ),
        migrations.AlterField(
            model_name='tweetrun',
            name='label',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='tweetrun',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 19, 20, 1, 47, 18260)),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 20, 1, 47, 19310)),
        ),
    ]
