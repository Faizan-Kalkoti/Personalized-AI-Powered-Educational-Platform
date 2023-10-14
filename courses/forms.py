from django import forms
from accounts.models import Student, Teacher
from courses.models import Course, Course_members

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'course_img')
        labels = {
            'course_name': 'Course Name',
            'course_description': 'Course Description',
            'course_img': 'Course Image',
        }
