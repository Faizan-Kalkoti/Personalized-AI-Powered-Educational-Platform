from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from accounts.models import Teacher, Student
from courses.models import Course, Course_members
from django.contrib.auth import get_user_model

User = get_user_model()

class Section(models.Model):
    section_name = models.CharField(max_length=200)
    section_description = models.CharField(max_length=200)
    belong_to_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contains_sections')
    students_completed = models.ManyToManyField(Student, through='Section_completed', related_name='sections_completed')
    available_to_student = models.ManyToManyField(Student, through='Available_sections')
    Accessible_at_level = [('Easy','Easy'),
                          ('Medium','Medium'),
                          ('Hard','Hard'),
                          ('Expert','Expert')] 
    Difficulty = models.CharField(max_length=20, choices=Accessible_at_level, default='Easy')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.section_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.section_name)
            unique_slug = base_slug
            counter = 1
            while Section.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    

    
class Section_completed(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
         unique_together = ("student", "section")


class Available_sections(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='available_sections')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students_with_access')

    class Meta:
         unique_together = ("student", "section")

# To deal with the accessed course objects 
# 1. student1 = Section.objects.all().first()
# 2. course1 = Course.objects.all().last()

# 3. Section.objects.create(section_name ="section 1", section_description="section to play twice to test slug", belong_to_course = course1)

# 4. sections_with_access = student1.available_sections.all()
# 5. sections_with_access.first().section                       -> here it returns section object that is related to the student (First one)
# 6. sections_with_access.first().section.section_name          -> here we get the name for the section name