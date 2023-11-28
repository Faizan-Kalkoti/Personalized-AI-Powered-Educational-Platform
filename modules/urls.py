from django.urls import path
from modules import views

app_name='modules'

urlpatterns =[
   path('create-module/<slug:course_slug>/<slug:section_slug>/',views.CreateModule.as_view(), name='createmodule'), 
   path('detail-module/<slug:course_slug>/<slug:section_slug>/<slug:slug>/', views.DetailModule.as_view(), name='detailmodule'),
]
