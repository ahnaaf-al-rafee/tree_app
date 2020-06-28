from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course, name='course'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]