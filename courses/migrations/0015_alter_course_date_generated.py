# Generated by Django 4.1 on 2023-11-02 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_course_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_generated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 2, 9, 39, 440981, tzinfo=datetime.timezone.utc)),
        ),
    ]
