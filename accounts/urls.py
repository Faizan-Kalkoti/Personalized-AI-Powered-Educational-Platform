from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.register, name='register'),
    path('student-signup/', views.SignupforStudent.as_view(), name='studentsignup'),
    path('teacher-signup/', views.SignupforTeacher.as_view(), name='teachersignup'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Rest API
    path('change-pic/',views.ChangePicAPIView, name='updateprofilephoto'),

    # For Ajax Request
    path('generate-OTP/', views.generateOTP, name="generateotp"),
    path('verify-top/', views.verify_OTP, name="verifyotp"),
]

# urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
