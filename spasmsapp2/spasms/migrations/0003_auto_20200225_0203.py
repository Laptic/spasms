# Generated by Django 3.0.3 on 2020-02-25 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spasms', '0002_auto_20200221_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('logo', models.FilePathField(path='/img')),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField()),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='num_posts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=250)),
                ('province', models.CharField(max_length=250)),
                ('language', models.CharField(max_length=250)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spasms.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='TweetRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('exercise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spasms.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('creation_time', models.DateTimeField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spasms.TwitterUser')),
                ('hashtags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spasms.HashTag')),
            ],
        ),
        migrations.AddField(
            model_name='hashtag',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spasms.TwitterUser'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spasms.Exercise'),
        ),
    ]
