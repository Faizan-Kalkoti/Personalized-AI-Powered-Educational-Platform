from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import Teacher, Student


from pytz import timezone
import pytz
from datetime import timedelta
from django.utils import timezone

User = get_user_model()

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    made_by_teacher = models.ForeignKey(to=Teacher , on_delete=models.CASCADE, related_name='made_course')
    student = models.ManyToManyField(Student ,through='Course_members', related_name='has_course') # To get through the model name
    course_img = models.ImageField(upload_to='photos/courses',blank=True) # to change the upload path
    course_description = models.CharField(max_length=300)
    slug = models.SlugField()
    iscomplete = models.BooleanField(default=False)

    Age_choices = [
        ('Age < 10', 'Age <10'),
        ('10 < Age < 15', '10 < Age < 15'),
        ('15 < Age < 18','15 < Age < 18'),
        ('Above 18', 'Above 18'),
        ('For all ages', 'For all ages'),]
    age_group = models.CharField(max_length=20, choices=Age_choices, default='For all ages')




    # for time in courses
    tz1 = pytz.timezone('Asia/Kolkata')
    current_time = timezone.now().astimezone(tz1)
    duration = timedelta(hours=5, minutes=30)
    current_date = current_time + duration
    date_generated = models.DateTimeField(default=current_date)
    

    def __str__(self):
        return self.course_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.course_name)
            unique_slug = base_slug
            counter = 1
            while Course.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        if not self.made_by_teacher:
           self.made_by_teacher = self.request.user.teacher
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["course_name"]
    

class Course_members(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='part_of')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_groups')

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ("student", "course")

# Create your models here.
