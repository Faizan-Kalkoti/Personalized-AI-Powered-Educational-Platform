from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import (BaseUserForm, TeacherRegistrationForm, 
                    StudentRegistrationForm)



def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')



# form for Student registration
class SignupforTeacher(CreateView):
    template_name = 'registration/teacher_register.html'
    form_class = BaseUserForm
    success_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_form'] = TeacherRegistrationForm()
        return context
    
    def form_valid(self, form):
        profile_form = TeacherRegistrationForm(self.request.POST, self.request.FILES)
        
        if profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('accounts:login')
        else:
            return self.render_to_response(self.get_context_data(form=form, profile_form = profile_form))


# form for Student registration
class SignupforStudent(CreateView):
    template_name = 'registration/student_register.html'
    form_class = BaseUserForm
    success_url = reverse_lazy('accounts:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_form'] = StudentRegistrationForm()
        return context
    
    def form_valid(self, form):
        profile_form = StudentRegistrationForm(self.request.POST, self.request.FILES)
        
        if profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('accounts:login')
        else:
            return self.render_to_response(self.get_context_data(form=form, profile_form = profile_form))
# Create your views here.
