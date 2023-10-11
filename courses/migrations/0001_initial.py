# Generated by Django 4.1 on 2023-10-08 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_otpverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_img', models.ImageField(upload_to='photos/')),
                ('course_description', models.CharField(max_length=300)),
                ('date_generated', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('made_by_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_course', to='accounts.teacher')),
            ],
            options={
                'ordering': ['course_name'],
            },
        ),
        migrations.CreateModel(
            name='Course_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_groups', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_of', to='accounts.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(related_name='has_course', through='courses.Course_members', to='accounts.student'),
        ),
    ]