from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import (BaseUserForm, TeacherRegistrationForm, 
                    StudentRegistrationForm)

# All these required for OTP generation and verification
from django.http import JsonResponse
from accounts.models import OTPverification

from datetime import datetime, timedelta
from pytz import timezone
from django.utils import timezone
import random
import json
import pyotp

from pathlib import Path
from finalproject import settings
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

User = get_user_model()



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




# Views for OTP generation and verification
# For OTP generation
def generateOTP(request):
    # Generate a time-based OTP
    totp_secret = pyotp.random_base32()
    ztotp = pyotp.TOTP(totp_secret)
    totp = ztotp.now()

#    FOr time
    otp_generated_at = timezone.now()
    
    obj= {"result":"Updated and sent OTP!",
          "OTP":totp}

    param_name = request.GET.get('user_name', '')  # Get the value of 'param1' or an empty string if it's not present
    param_mail = request.GET.get('email', '')
    print("name: ", param_name)
    print("email: ", param_mail)


    try: 
        User.objects.get(email = param_mail)
        obj['result'] = 'User Email exists'
        obj['OTP'] = "no otp for you!"
        return JsonResponse(obj)
    except User.DoesNotExist:
        send_mail('Email varification OTP from AIEdu website',
              "The OTP to verify the email is as follows: \n"+"OTP: "+totp,
              'Faizan.AIedu@gmail.com',
              [param_mail],
              fail_silently =True)
        try:
           temp = OTPverification.objects.get(email_field = param_mail)
           temp.otp_field = totp
           temp.user_name = param_name
           temp.time_generated = otp_generated_at
           temp.save()

           obj['result'] = 'Email exists'
           obj['OTP'] = totp
           obj['time'] = timezone.now()
           return JsonResponse(obj)
        except OTPverification.DoesNotExist:
           otp_instance = OTPverification.objects.create(user_name = param_name, email_field=param_mail, otp_field = totp, time_generated = timezone.now())
           print(otp_instance.user_name)
           print(totp)
           return JsonResponse(obj)
        
# End of the OTP generation view





# Start of OTP verification view
def verify_OTP(request):  
 if request.method == 'POST':
    data = json.loads(request.body.decode('utf-8'))
    otp_entered = data['otp']
    param_mail = data['email']
    # otp_entered =  request.POST.get('otp')  # Get the OTP from here
    # param_mail = request.POST.get('email')  # Get teh mail from here
    time_elapsed = timezone.now()
    print("to check if this extracts mail properly: ", param_mail)
    print("If atleast OTP is extracted: ", otp_entered)
    try:
        get_obj = OTPverification.objects.get(email_field =param_mail)
        # print(param_mail)
        time_gen = get_obj.time_generated  
        time_diff =  time_elapsed - time_gen
        limit = timedelta(seconds = 30)
        if time_diff < limit:
            if get_obj.otp_field == otp_entered:
                print("this is the time elapsed: ", time_diff)
                result_obj = {
                        'verified':'yes',
                        'staticBackdropLabel' : "Email Verified Successfully",
                        'result_img':'photos/correct.jpg',
                        'result_btns': '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>&nbsp<button type="submit" class="btn btn-success">Sign up</button>'
                      } 
                get_obj.delete()
                return JsonResponse(result_obj)
            else:
                print("this is the time elapsed: ", time_diff)
                result_obj={
                        'verified':'no',
                        'staticBackdropLabel':"Verification Failed!",
                        'result_img':'photos/wrong.jpg',
                        'result_btns':'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
                     }
                return JsonResponse(result_obj)
        else:
            print("this is the time elapsed: ", time_diff)
            result_obj={
                    'verified':'no',
                    'staticBackdropLabel':"Verification Failed. Time Limit Exceeded!",
                    'result_img':'photos/wrong.jpg',
                    'result_btns':'<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
                }
            return JsonResponse(result_obj)
    except OTPverification.DoesNotExist:  
        result_obj={
                'verified':'no',
                'staticBackdropLabel' : "OTP Not sent!",
                'result_img':'photos/wrong.jpg',
                'result_btns': '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>'
             }
        return JsonResponse(result_obj)

# End of the OTP verification views

