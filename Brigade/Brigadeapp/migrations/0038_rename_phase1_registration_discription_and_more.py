# Generated by Django 4.2.1 on 2023-06-08 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brigadeapp', '0037_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='phase1',
            new_name='discription',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='title',
        ),
    ]
