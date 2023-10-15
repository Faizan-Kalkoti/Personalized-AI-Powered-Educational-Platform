from django.urls import path, include
from courses import views
from django.conf import settings

app_name = 'courses'

urlpatterns = [
    # All the courses for the view urls here
    path('', views.ListCourse.as_view(), name='allcourseslist'),
    path('create-course/', views.CreateCourse.as_view(), name="createcourse"),
    path('course-in/<slug:slug>/', views.SingleCourse.as_view(), name='singlecourse'),
    path('delete-course/<slug:slug>/', views.DeleteCourse.as_view(), name='deletecourse'),
    path('complete-course/<slug:slug>/', views.CourseCompleted.as_view(), name="coursecompleted"),
    path('join-course/<slug:slug>/', views.JoinCourse.as_view(), name="joincourse"),

    # User's dashboard links here
    path('teacher-dashboard/', views.Courses_of_teacher.as_view(), name="teacher_dashboard"),
]