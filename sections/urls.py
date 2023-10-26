from django.urls import path
from sections import views

app_name = 'sections'

urlpatterns=[
    path('create-section/<slug:slug>/',views.CreateSection.as_view(),name='createsection'),
    path('delete-section/<slug:slug>/', views.DeleteSection.as_view(), name='deletesection'),
    # path('list-sections/<slug:slug>/', views.ListSections.as_view(), name='listsection'),
]