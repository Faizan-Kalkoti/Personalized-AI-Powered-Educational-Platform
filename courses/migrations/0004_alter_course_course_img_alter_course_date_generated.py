# Generated by Django 4.1 on 2023-10-11 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_img',
            field=models.ImageField(blank=True, upload_to='photos/courses'),
        ),
        migrations.AlterField(
            model_name='course',
            name='date_generated',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 1, 51, 8, 50767, tzinfo=datetime.timezone.utc)),
        ),
    ]