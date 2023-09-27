from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Teacher, Student
from django.contrib.auth import get_user_model

class BaseUserForm(UserCreationForm):

    class Meta:
        fields= ('username', 'email')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Your Username"
        self.fields['email'].label = "Your Email"

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model  = Teacher
        fields = ('profile_photo', 'experience', 'gender', 'number', 'bio')

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_photo'].labels = "Upload you profile photo"
        self.fields['experience'].labels = "Select the number of year's experience"
        self.fields['gender'].labels = "Choose your gender"
        self.fields['number'].labels = "Enter your phone number"
        self.fields['bio'].labels = "Enter your description as a teacher"

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('profile_photo', 'bio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_photo'].labels = "Upload you profile photo"
        self.fields['bio'].labels = "Enter your bio"