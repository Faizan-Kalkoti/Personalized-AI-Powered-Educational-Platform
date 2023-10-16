from django.db import models
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

    def __str__(self):
        return self.section_name
    

    
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

