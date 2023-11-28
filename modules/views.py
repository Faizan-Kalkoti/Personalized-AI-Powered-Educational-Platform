from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


from django.db import IntegrityError
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from accounts.models import Student, Teacher
from courses.models import Course, Course_members
from sections.models import Section, Available_sections
from modules.models import Module, Module_completed

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields =('module_name', 'module_content', 'module_image', 'module_video')
        label ={
            'module_name' : 'Name of The Lesson',
            'module_content' : 'Content of the Lesson',
            'module_image' : 'Add Image',
            'module_video': 'Add Video',
        }

# 1. CreateModule
class CreateModule(LoginRequiredMixin, CreateView):
    template_name = 'modules/create_modules.html'
    model = Module
    form_class = ModuleForm
    context_object_name = 'module'

    def form_valid(self, form):
        course_slug = self.kwargs.get('course_slug')
        section_slug = self.kwargs.get('section_slug')
        if course_slug:
             try:
                 course1 = Course.objects.get(slug=course_slug)
                 section1 = Section.objects.get(slug =section_slug)
                 form.instance.belong_to_course = course1
                 form.instance.part_of_section = section1
             except Course.DoesNotExist:
                 return HttpResponseRedirect('/error_url/')
        slug = form.instance.slug
        count = 1
        while Course.objects.filter(slug=slug).exists():
            slug = f"{form.instance.slug}-{count}"
            count += 1
            form.instance.slug = slug
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_slug = self.kwargs.get('course_slug')
        if course_slug:
             try:
                 course1 = Course.objects.get(slug=course_slug)
             except:
                 course1 = None
                 return HttpResponseRedirect('/error_url/')  
        # Add additional data to the context
        context['course'] = course1
        return context
   
    def get_success_url(self):
        course_slug = self.kwargs.get('course_slug')
        return reverse('courses:singlecourse', kwargs={'slug': course_slug})
    
    # def get_initial(self):
    #     initial = super().get_initial()
    #     # Add fields and their initial values to the initial dictionary
    #     initial['field_name'] = 'initial_value'
    #     return initial

# # 2. UpdateModule
# class UpdateModule(LoginRequiredMixin, UpdateView):
#     pass

# # 3. DeleteModule
# class DeleteModule(LoginRequiredMixin, DeleteView):
#     pass

# 4. DetailModule
class DetailModule(LoginRequiredMixin, DetailView):
    template_name = 'modules/detail_modules.html'
    context_object_name = 'module'
    model = Module
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section_slug = self.kwargs.get('section_slug')
        course_slug = self.kwargs.get('course_slug')

        Section1 = Section.objects.get(slug = section_slug) 
        Course1 = Course.objects.get(slug=course_slug)
        
        context['section'] = Section1
        context['course'] = Course1
        return context


