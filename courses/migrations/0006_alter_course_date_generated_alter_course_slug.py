# Generated by Django 4.1 on 2023-10-14 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_generated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 19, 10, 35, 445941, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
