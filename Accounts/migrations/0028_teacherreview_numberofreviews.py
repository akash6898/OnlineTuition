# Generated by Django 3.0.8 on 2020-09-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0027_teacherreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherreview',
            name='numberOfReviews',
            field=models.IntegerField(default=0),
        ),
    ]
