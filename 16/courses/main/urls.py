import signup as signup
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('courses', views.courses, name='courses'),
    path('subject', views.subject, name='subject'),
    path('instructor', views.instructor, name='instructor'),
    path('table', views.table, name='table'),
    path('add_courses/', views.add_courses, name='add_courses'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_instructor/', views.add_instructor, name='add_instructor'),
    path('users/', include('django.contrib.auth.urls')),
]
