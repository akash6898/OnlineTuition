# Generated by Django 3.0.8 on 2020-08-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_merge_20200727_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutordetails',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]
