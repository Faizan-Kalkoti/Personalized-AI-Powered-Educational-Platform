# Generated by Django 4.1 on 2023-10-16 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_course_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_generated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 0, 57, 36, 858429, tzinfo=datetime.timezone.utc)),
        ),
    ]
