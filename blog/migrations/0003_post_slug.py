# Generated by Django 4.1.1 on 2022-12-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='dd', unique=True),
            preserve_default=False,
        ),
    ]