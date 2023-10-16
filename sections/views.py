from django.shortcuts import render
from django.db.models.query import QuerySet
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from courses.models import Course, Course_members
from sections.models import Section, Section_completed, Available_sections
from accounts.models import Student, Teacher

from django.views.generic import (CreateView, RedirectView, UpdateView,
                                  ListView, DeleteView, DetailView)



# Create your views here.
# 1. Create Sections
# 2. List Sections (that are available)
# 3. List Sections (that are not-avalaible without links )
# 4. List all sections without Links (for students that are not logged in)

# 5. Update Sections
# 6. Delete Sections
# 7. Detail Sections
# 8. Section completed by student
# 9. Section accessible to student

