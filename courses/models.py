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
    course_img = models.ImageField(upload_to='photos/courses') # to change the upload path
    course_description = models.CharField(max_length=300)
    tz1 = pytz.timezone('Asia/Kolkata')
    current_time = timezone.now().astimezone(tz1)
    duration = timedelta(hours=5, minutes=30)
    current_date = current_time + duration
    date_generated = models.DateTimeField(default=current_date)
    # date_generated = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.course_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        # self.g_description_html = misaka.html(self.g_description)
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
