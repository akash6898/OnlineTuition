# Generated by Django 3.0.8 on 2020-07-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_tutordetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='loggedIn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='loggedOut',
            field=models.BooleanField(default=False),
        ),
    ]
