# Generated by Django 3.0.8 on 2021-03-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='author',
        ),
    ]
