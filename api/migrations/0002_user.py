# Generated by Django 3.1 on 2020-10-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('accessId', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=128)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
