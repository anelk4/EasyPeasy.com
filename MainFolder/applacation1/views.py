from django.shortcuts import render



def courses(request):
    return render(request,'applacation1/courses.html')




def home(request):
    return render(request,'applacation1/home.html')




def profile(request):
    return render(request,'applacation1/profile.html')
