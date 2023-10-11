from django.contrib import admin
from courses.models import Course, Course_members

admin.site.register(Course)
admin.site.register(Course_members)

# Register your models here.
