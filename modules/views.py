from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.db import IntegrityError
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from accounts.models import Student, Teacher
from courses.models import Course, Course_members
from sections.models import Section, Available_sections
from modules.models import Module, Module_completed

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView



# 1. CreateModule
# 2. UpdateModule
# 3. DeleteMudule
# 4. DetailModule

# Create your views here.
