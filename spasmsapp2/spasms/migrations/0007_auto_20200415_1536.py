# Generated by Django 3.0.3 on 2020-04-15 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spasms', '0006_auto_20200415_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetrun',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 15, 36, 55, 239883)),
        ),
        migrations.AlterField(
            model_name='tweetrun',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 15, 36, 55, 239854)),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 15, 36, 55, 241725)),
        ),
    ]
