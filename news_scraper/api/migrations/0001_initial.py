# Generated by Django 3.2 on 2021-04-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
    ]