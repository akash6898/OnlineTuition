# Generated by Django 3.0.8 on 2020-08-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0009_remove_tutordetails_specialitycourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutordetails',
            name='userName',
            field=models.CharField(default='noidea', max_length=100),
            preserve_default=False,
        ),
    ]
