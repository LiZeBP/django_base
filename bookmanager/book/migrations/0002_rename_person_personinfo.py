# Generated by Django 4.1 on 2022-08-28 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='PersonInfo',
        ),
    ]
