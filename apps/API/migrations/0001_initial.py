# Generated by Django 4.1.2 on 2022-10-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=70)),
                ('color', models.CharField(default='', max_length=40)),
                ('description', models.CharField(default='', max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
