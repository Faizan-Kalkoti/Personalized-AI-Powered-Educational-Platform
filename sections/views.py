from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db.models.query import QuerySet
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django import forms

from django.contrib.auth.decorators import login_required

from courses.models import Course, Course_members
from sections.models import Section, Section_completed, Available_sections
from accounts.models import Student, Teacher

from django.views.generic import (CreateView, RedirectView, UpdateView,
                                  ListView, DeleteView, DetailView)


class SectionForm(forms.ModelForm):
   class Meta:
      model = Section
      fields = ('section_name', 'section_description', 'Difficulty' )
      label = {
         'section_name': 'Name of the section',
         'section_description':'Description',
         'Difficulty':'Set Difficulty',
      }


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


class CreateSection(LoginRequiredMixin,SelectRelatedMixin , CreateView):
   template_name = 'sections/section_form.html'
   model = Section
   form_class = SectionForm

   def form_valid(self, form):
        course_slug = self.kwargs.get('slug')
        if course_slug:
             try:
                 course1 = Course.objects.get(slug=course_slug)
                 form.instance.belong_to_course = course1
             except Course.DoesNotExist:
                 return HttpResponseRedirect('/error_url/')
        slug = form.instance.slug
        count = 1
        while Course.objects.filter(slug=slug).exists():
            slug = f"{form.instance.slug}-{count}"
            count += 1
            form.instance.slug = slug
        return super().form_valid(form)
   
   def get_success_url(self):
        course = self.kwargs.get('slug')
        return reverse('courses:singlecourse', kwargs={'slug': course})
   
   
   
class DeleteSection(LoginRequiredMixin , DeleteView):
    template_name='sections/section_delete.html'
    model = Section
    success_url = reverse_lazy('courses:allcourseslist')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(slug = self.kwargs['slug'])
    
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
    
class UpdateSection(UpdateView):
    template_name="sections/update_section.html"
    model = Section
    form_class = SectionForm
    slug_field = 'slug'  # Specify the slug field used in your model

    def get_object(self, queryset=None):
        # Retrieve the Section instance based on the slug in the URL
        section_slug = self.kwargs.get('section_slug')
        return Section.objects.get(slug=section_slug)

    def get_success_url(self):
        course_slug = self.kwargs.get('course_slug')
        print(course_slug)
        return reverse('courses:singlecourse', kwargs={'slug': course_slug})

    


# class ListSections(ListView):
#     template_name = 'courses/course_detail.html'
#     model = Section
    # context_object_name = 'sections'

    # def get_queryset(self):
    #     queryset = Section.objects.all()
    #     course_slug = self.kwargs.get('slug')

    #     if course_slug:
    #          try:
    #              course1 = Course.objects.get(slug=course_slug)
    #          except Course.DoesNotExist:
    #              course1 = None

    #     if course1:
    #         queryset = Section.objects.filter(belong_to_course=course1)
    #         print(queryset)
    #     return queryset