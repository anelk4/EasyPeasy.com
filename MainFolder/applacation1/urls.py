from django.urls import path,include
from . import views
#from django .views.generic import TemplateView
#from django.conf import settings
#from django.conf.urls.static import static
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
    path('watch_video/',views.watch_video, name='watch_video'),
    path('',include('django.contrib.auth.urls')),

]


