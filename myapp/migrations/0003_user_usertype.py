# Generated by Django 4.1.4 on 2022-12-31 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='buyer', max_length=100),
        ),
    ]
