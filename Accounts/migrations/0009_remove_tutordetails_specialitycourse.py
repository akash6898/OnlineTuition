# Generated by Django 3.0.8 on 2020-08-03 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_tutordetails_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutordetails',
            name='specialityCourse',
        ),
    ]
