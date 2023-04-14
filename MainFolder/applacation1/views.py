from django.shortcuts import render


def courses(request):
    return render(request,'applacation1/courses.html')



def home(request):
    return render(request,'applacation1/home.html')



def profile(request):
    return render(request,'applacation1/profile.html')



def login(request):
    return render(request,'applacation1/login.html')



def update(request):
    return render(request,'applacation1/update.html')




def degister(request):
    return render(request,'applacation1/degister.html')

