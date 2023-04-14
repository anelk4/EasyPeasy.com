from django.urls import path
from . import views
urlpatterns = [
    path('courses/',views.courses, name='courses'),
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile')
]