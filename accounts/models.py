from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='teacher')
    is_verified = models.BooleanField(default=False)
    number = models.CharField(max_length=11)
    profile_photo = models.ImageField(upload_to='photos/teacher', null=True, blank=True)
    bio = models.CharField(max_length=100, blank=True, null=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')]
    
    EXPERIENCE_CHOICES=[
        ('less then 1 year','less then 1 year'),('1 - 2 years','1 - 2 years'),
        ('2-4 years','2-4 years'),('5 years and above','5 years and above'),
    ]

    TYPE_USER = [
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('admin', 'admin')]
    is_type = models.CharField(max_length=20, choices=TYPE_USER, default='teacher')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='None')
    experience = models.CharField(max_length=30, choices=EXPERIENCE_CHOICES, default='less then 1 year')
    # resume  =models.FileField(upload_to='pdfs/')

    def save(self, *args, **kwargs):
        self.name = self.user.username
        self.is_type = 'teacher'
        super().save(*args, **kwargs)

    def to_verify_teacher(self):
        self.is_verified = True
        self.save()

    def __str__(self):
        return self.name




class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='student')

    TYPE_USER = [
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('admin', 'admin')]
    
    is_type = models.CharField(max_length=20, choices=TYPE_USER, default='student')
    profile_photo = models.ImageField(upload_to='photos/student', null=True, blank=True)
    bio = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.user.username
        self.is_type = 'student'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    
# For verifying OTP through rest apis or json views
class OTPverification(models.Model):
    user_name = models.CharField(max_length=100)
    email_field = models.EmailField(unique=True)
    otp_field = models.CharField(max_length=6)
    time_generated = models.DateTimeField()
    is_OTP_verfified = models.BooleanField(default=False)

    def __str__(self):
        return self.otp_field