# Generated by Django 4.1 on 2023-10-16 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_course_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_generated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 16, 20, 51, 16, 83271, tzinfo=datetime.timezone.utc)),
        ),
    ]
