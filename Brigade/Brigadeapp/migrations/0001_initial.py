# Generated by Django 4.1.7 on 2023-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enquire_now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('Last_name', models.CharField(default='', max_length=20)),
                ('Mobile_number', models.IntegerField(default='')),
                ('email', models.EmailField(default='', max_length=20)),
            ],
        ),
    ]
