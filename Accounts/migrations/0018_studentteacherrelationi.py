# Generated by Django 3.0.8 on 2020-08-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0017_auto_20200804_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentTeacherRelationi',
            fields=[
                ('studentEmailId', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('teacherEmailId', models.TextField(max_length=10000)),
            ],
        ),
    ]
