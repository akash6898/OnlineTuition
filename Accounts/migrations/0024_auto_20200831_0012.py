# Generated by Django 3.0.8 on 2020-08-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0023_auto_20200827_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutordetails',
            name='profilePhoto',
            field=models.ImageField(upload_to='studentProfile'),
        ),
    ]