# Generated by Django 3.2.9 on 2021-11-16 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='image',
            new_name='images',
        ),
    ]
