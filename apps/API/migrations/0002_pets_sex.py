# Generated by Django 4.1.2 on 2022-10-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='sex',
            field=models.CharField(default='', max_length=10),
        ),
    ]
