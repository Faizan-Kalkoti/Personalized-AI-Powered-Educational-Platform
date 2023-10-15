from django.db import models
from accounts.models import Teacher, Student
from courses.models import Course, Course_members

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
