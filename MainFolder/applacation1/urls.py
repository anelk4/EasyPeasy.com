from django.urls import path
from . import views
urlpatterns = [
    path('courses/',views.courses, name='courses'),
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('login/',views.login, name='login'),
    path('update/',views.update, name='update'),
    path('degister/',views.degister, name='degister'),
    path('contact/',views.contact, name='contact'),
    path('dabout/',views.dabout, name='dabout'),
    path('kuratori/',views.kuratori, name='kuratori'),
    path('playlist/',views.playlist, name='playlist'),
    path('teacher_profile/',views.teacher_profile, name='teacher_profile'),
    path('watchvideo/',views.watchvideo, name='watchvideo')
]



