from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import Teacher, Student
from sections.models import Section
from courses.models import Course, Course_members

from pytz import timezone
from datetime import timedelta
from django.utils import timezone

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    module_video = models.FileField(blank=True, upload_to='videos/modules', null=True)
    module_content = models.CharField(max_length=1000)
    module_image = models.ImageField(blank=True, upload_to='photos/modules')
    slug = models.SlugField()
   
    is_completed = models.ManyToManyField(Student, through='Module_completed', related_name='modules_completed')
    part_of_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='has_modules')
    belong_to_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contains_modules')

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.module_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.module_name)
            unique_slug = base_slug
            counter = 1
            while Module.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        if not self.belong_to_course:
            if hasattr(self, 'course'):
                self.belong_to_course = self.course
            else:
                raise ValueError("Course information not provided.")
            
        if not self.part_of_section:
            if hasattr(self, 'section'):
                self.part_of_section = self.section
            else:
                raise ValueError("Section information not provided.")
        super().save(*args, **kwargs)


# ManytoManyfield

class Module_completed(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    class Meta:
         unique_together = ("student", "module")
