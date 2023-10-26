"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from finalproject import views
from accounts import views as vs

urlpatterns = [
    # these are the urls that lead to other apps in the project
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('sections/', include('sections.urls', namespace='sections')),

    # this are the base project related views
    path('', views.index, name='index'),
    path('django/', views.djangocontent, name='djangocontent'),
    path('email-attachment/', views.send_with_attachment, name="emailattachment"),
    path('django-email/', views.base, name='djangoemail'),
    path('about/', views.aboutview, name='about'),
    # path('authentication/', include('registration.urls', namespace='registration')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
