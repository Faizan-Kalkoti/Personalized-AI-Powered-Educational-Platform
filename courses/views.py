from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from courses.models import Course, Course_members
from django.views.generic import (CreateView, RedirectView, UpdateView,
                                  ListView, DeleteView, DetailView)
from accounts.models import Teacher, Student

# for pagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




# Create your views here.
# 1. CreateCourse
# 2. Join Course (for students) - Custom views
# 3. Leave Course (for students) - Custom views // 'not necessary here'
# 4. Delete Course (for Teachers)
# 5. List out all the courses (made by the teacher)
# 6. Detail of the courses.

class CourseForm(forms.ModelForm):
    course_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50})
    )
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'course_img', 'age_group')
        labels = {
            'course_name': 'Course Name',
            'course_description': 'Course Description',
            'course_img': 'Course Image',
            'age_group': 'Age Group',
        }

class CreateCourse(LoginRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course
    template_name = 'courses/course_form.html'

    def form_valid(self, form):
        # Retrieve the logged-in user's teacher profile
        teacher_profile = self.request.user.teacher  # Assuming 'teacher' is the related name
        form.instance.made_by_teacher = self.request.user.teacher

        slug = form.instance.slug
        count = 1
        while Course.objects.filter(slug=slug).exists():
            slug = f"{form.instance.slug}-{count}"
            count += 1
            form.instance.slug = slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('courses:allcourseslist')
    

class SingleCourse(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class ListCourse(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = Course.objects.all()
        name= self.request.GET.get('name', None)
        print(name)
        try:
           teacher1 = self.request.user.teacher
        except (ObjectDoesNotExist, AttributeError):
           teacher1 = None
        # print(teacher1)

        if name:
            queryset = queryset.filter(course_name__contains=name)
        queryset = queryset.filter(iscomplete=True)
        return queryset

class DeleteCourse(LoginRequiredMixin, DeleteView):
    template_name = 'courses/course_delete.html'
    model = Course
    success_url = reverse_lazy('courses:allcourseslist')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(slug = self.kwargs['slug'])
    
    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Courses Deleted!')
        return super().delete(*args, **kwargs)



class JoinCourse(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("courses:singlecourse",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course,slug=self.kwargs.get("slug"))
        student = get_object_or_404(Student, name = self.request.user.username)
        # print(student)
        try:
            Course_members.objects.create(student=student,course=course)
        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(course.course_name)))
        else:
            messages.success(self.request,"You are now a member of the {} group.".format(course.course_name))

        return super().get(request, *args, **kwargs)
    


class CourseCompleted(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs):
        return reverse("courses:singlecourse",kwargs={"slug": self.kwargs.get("slug")})
    
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs.get("slug"))
        course.iscomplete = True
        course.save()
        return super().get(request, *args, **kwargs)

class Courses_of_teacher(ListView):
    model = Course
    template_name = 'auth/teacher_dashboard.html'
    context_object_name = 'courses'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Course.objects.all()
        try:
           teacher1 = self.request.user.teacher
        except (ObjectDoesNotExist, AttributeError):
           teacher1 = None
        print(teacher1)
        queryset = queryset.filter(made_by_teacher=teacher1)
        print(queryset)
        return queryset
    

class UpdateCourse(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/update_course.html'
    success_url = reverse_lazy('courses:allcourseslist')
    




# class LeaveCourse(LoginRequiredMixin, RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse("courses:single",kwargs={"slug": self.kwargs.get("slug")})

#     def get(self, request, *args, **kwargs):
#         try:
#             membership = Course_members.objects.filter(user=self.request.user,
#                                                     course__slug=self.kwargs.get("slug")).get()
#         except Course_members.DoesNotExist:
#             messages.warning( self.request,
#                               "You can't leave this course because you aren't in it." )
#         else:
#             membership.delete()
#             messages.success( self.request,
#                               "You have successfully left this course." )
            
#         return super().get(request, *args, **kwargs)
