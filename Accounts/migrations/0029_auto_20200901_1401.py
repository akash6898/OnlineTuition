# Generated by Django 3.0.8 on 2020-09-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0028_teacherreview_numberofreviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherreview',
            name='numberOfReviews',
            field=models.BooleanField(default=True),
        ),
    ]
